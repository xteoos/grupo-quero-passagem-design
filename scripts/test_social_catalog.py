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
  source=json.loads((S.parents[1]/'fontes-de-origem/figma-previews.json').read_text());original={F+a['id']for a in source if a['fileKey']=='EyJUWysTaFKnJewVXFz0u0'}
  removed=json.loads((S.parents[1]/'fontes-de-origem/retirados-do-catalogo.json').read_text());archived={a['id']for a in removed}
  self.assertEqual(len(original),280);self.assertTrue(original.issubset(set(A)|archived))
  rows=[a for id,a in A.items()if id in original]
  self.assertTrue(all(a.get('review_level')and a.get('composition_role')and a.get('source_name')for a in rows))
 def test_simplified_qp_categories(self):
  qp=[a for a in A.values()if a['brand']=='quero-passagem']
  self.assertFalse(any(a['category']in['cidades','fundos','pranchas-de-elementos']for a in qp))
  self.assertGreaterEqual(sum(a['category']=='stickers'for a in qp),42)
  self.assertEqual(sum(a.get('asset_kind')=='ilustracao-de-cidade'for a in qp),6)
 def test_sheet_children_and_interactive_profile(self):
  self.assertEqual(A[F+'2464:8338']['category'],'stickers');self.assertEqual(A[F+'2469:2605']['category'],'stickers')
  profile=json.loads((S/'references/social/familias.json').read_text())['profiles'][0];self.assertFalse(profile['photo_required']);self.assertEqual(len(profile['fields']),4)
  for id in profile['sticker_ids']+[profile['path_id'],profile['pattern_id']]:self.assertIn(id,A)
if __name__=='__main__':unittest.main()
