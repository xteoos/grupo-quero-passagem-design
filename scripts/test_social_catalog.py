import json,pathlib,unittest
S=pathlib.Path(__file__).resolve().parents[1]/'skills/qp-brandbook';A={a['id']:a for a in json.loads((S/'references/assets-index.json').read_text())['assets']};F='figma:EyJUWysTaFKnJewVXFz0u0:'
class SocialCatalogTests(unittest.TestCase):
 def test_color_guides_are_not_templates(self):
  for id in ['2176:116','2176:119','2176:122','1:4175','2202:110']:
   self.assertEqual(A[F+id]['category'],'guias-de-cores')
 def test_specific_composition_elements_are_discoverable(self):
  for id,category,term in [('176:6','linhas-e-percursos','percurso'),('66:27','letterings','Bacalar'),('2150:243','stickers','postal'),('2150:238','stickers','Ônibus'),('1:4176','pranchas-de-elementos','mexicanos'),('2202:114','letterings','Rodon')]:
   a=A[F+id];self.assertEqual(a['category'],category);self.assertIn(term.casefold(),a['name'].casefold());self.assertTrue(a['composition_role']);self.assertTrue(a['source_name'])
 def test_family_examples_are_complete_pieces_from_the_right_brand(self):
  for family in json.loads((S/'references/social/familias.json').read_text())['families']:
   for id in family['references']:
    a=A[id];self.assertEqual(a['brand'],family['brand']);self.assertEqual(a['category'],'pecas-sociais');self.assertEqual(a['family'],family['id'])
   for id in family['elements']:self.assertNotEqual(A[id]['category'],'pecas-sociais')
 def test_entire_social_export_has_review_metadata(self):
  rows=[a for id,a in A.items()if id.startswith(F)]
  self.assertEqual(len(rows),280)
  self.assertTrue(all(a.get('review_level')and a.get('composition_role')and a.get('source_name')for a in rows))
if __name__=='__main__':unittest.main()
