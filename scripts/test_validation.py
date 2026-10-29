import hashlib,pathlib,tempfile,unittest
from validate import inspect_file
class IntegrityTests(unittest.TestCase):
    def test_missing_original_is_not_a_valid_asset(self):
        with tempfile.TemporaryDirectory()as d:self.assertEqual(inspect_file(pathlib.Path(d)/"missing.png"),"missing")
    def test_lfs_pointer_is_not_image_bytes(self):
        with tempfile.TemporaryDirectory()as d:
            p=pathlib.Path(d)/"photo.jpg";p.write_text("version https://git-lfs.github.com/spec/v1\noid sha256:"+"0"*64+"\nsize 123\n")
            self.assertEqual(inspect_file(p),"lfs-pointer")
    def test_mutated_asset_fails_hash_check(self):
        with tempfile.TemporaryDirectory()as d:
            p=pathlib.Path(d)/"file";p.write_bytes(b"changed")
            self.assertEqual(inspect_file(p,hashlib.sha256(b"original").hexdigest()),"hash-mismatch")
    def test_original_matches_and_empty_file_fails(self):
        with tempfile.TemporaryDirectory()as d:
            p=pathlib.Path(d)/"file";p.write_bytes(b"original")
            self.assertIsNone(inspect_file(p,hashlib.sha256(b"original").hexdigest()))
            p.write_bytes(b"");self.assertEqual(inspect_file(p),"empty")
if __name__=="__main__":unittest.main()
