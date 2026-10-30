import hashlib,json,pathlib,sys,tempfile,unittest
from unittest.mock import patch
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'skills/qp-brandbook/scripts'))
import remote_assets as remote
class RemoteTests(unittest.TestCase):
 def setup_root(self,folder,content,path='assets/file.png',lfs=False):
  root=pathlib.Path(folder);(root/remote.STATE).write_text(json.dumps({'commit':'a'*40,'files':{path:{'sha256':hashlib.sha256(content).hexdigest(),'bytes':len(content),'lfs':lfs}}}));return root
 def test_verified_lfs_and_reuse(self):
  with tempfile.TemporaryDirectory()as d:
   root=self.setup_root(d,b'image',lfs=True)
   with patch.object(remote,'request',return_value=b'image')as req:
    remote.fetch('assets/file.png',root);remote.fetch('assets/file.png',root)
    self.assertEqual(req.call_count,1);self.assertIn('media.githubusercontent.com/media/',req.call_args.args[0])
 def test_corrupt_cached_file_is_refetched(self):
  with tempfile.TemporaryDirectory()as d:
   root=self.setup_root(d,b'image');p=root/'assets/file.png';p.parent.mkdir();p.write_bytes(b'bad')
   with patch.object(remote,'request',return_value=b'image'):remote.fetch('assets/file.png',root)
   self.assertEqual(p.read_bytes(),b'image')
 def test_pointer_and_wrong_bytes_rejected(self):
  for payload in [b'version https://git-lfs.github.com/spec/v1\n',b'wrong']:
   with tempfile.TemporaryDirectory()as d:
    root=self.setup_root(d,b'image')
    with patch.object(remote,'request',return_value=payload),self.assertRaises(ValueError):remote.fetch('assets/file.png',root)
    self.assertFalse((root/'assets/file.png').exists())
 def test_path_cannot_escape_package(self):
  with tempfile.TemporaryDirectory()as d,self.assertRaises(ValueError):remote.local(pathlib.Path(d),'../escape')
 def test_css_dependencies_downloaded(self):
  with tempfile.TemporaryDirectory()as d:
   css=b"@font-face{src:url('./font.ttf')}";root=self.setup_root(d,css,'assets/fonts.css');state=json.loads((root/remote.STATE).read_text());state['files']['assets/font.ttf']={'sha256':hashlib.sha256(b'font').hexdigest(),'bytes':4,'lfs':False};(root/remote.STATE).write_text(json.dumps(state))
   with patch.object(remote,'request',side_effect=[css,b'font']):remote.fetch('assets/fonts.css',root)
   self.assertEqual((root/'assets/font.ttf').read_bytes(),b'font')
if __name__=='__main__':unittest.main()
