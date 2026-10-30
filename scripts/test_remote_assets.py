import hashlib,json,pathlib,sys,tempfile,unittest
from unittest.mock import patch
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'skills/qp-brandbook/scripts'))
import remote_assets as remote
class RemoteTests(unittest.TestCase):
 def test_local_review_never_requests_github_and_persists(self):
  with tempfile.TemporaryDirectory()as d:
   base=pathlib.Path(d);source=base/'repo';dest=base/'installed';dest.mkdir();(source/'distribution').mkdir(parents=True);asset=source/'skills/qp-brandbook/assets/test.png';asset.parent.mkdir(parents=True);asset.write_bytes(b'local')
   bundle={'schema_version':1,'references':{'references/assets-index.json':'{"assets":[]}'},'files':{'assets/test.png':{'sha256':hashlib.sha256(b'local').hexdigest(),'bytes':5,'lfs':False}}};(source/'distribution/brandbook-bundle.json').write_text(json.dumps(bundle))
   with patch.object(remote,'request',side_effect=AssertionError('Rede não permitida no teste local')):
    self.assertEqual(remote.sync(dest,local_root=source)['mode'],'local-review');self.assertEqual(remote.sync(dest)['mode'],'local-review');remote.fetch('assets/test.png',dest)
   self.assertEqual((dest/'assets/test.png').read_bytes(),b'local')
 def test_return_to_github_is_explicit(self):
  with tempfile.TemporaryDirectory()as d:
   dest=pathlib.Path(d);(dest/remote.STATE).write_text(json.dumps({'source_root':'/unavailable-local-source'}));bundle={'schema_version':1,'references':{},'files':{}}
   with patch.object(remote,'request',side_effect=[json.dumps({'sha':'a'*40}).encode(),json.dumps(bundle).encode()]):self.assertEqual(remote.sync(dest,github=True)['mode'],'github')
   self.assertNotIn('source_root',json.loads((dest/remote.STATE).read_text()))
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
