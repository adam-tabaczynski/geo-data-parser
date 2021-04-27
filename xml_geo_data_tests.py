import unittest
from xml_geo_data import *

class GeoDataTests(unittest.TestCase):
  parsed_file_1 = parse_data('./parcel_aaa.xml')
  parsed_file_2 = parse_data('./parcel_nas.xml')
  parsed_file_3 = parse_data('./parcel_aaa_changed.xml')
  
  plot_of_land_1 = get_list_of_plots(parsed_file_1, 'Flurstueck')[0]
  plot_of_land_2 = get_list_of_plots(parsed_file_2, 'AX_Flurstueck')[0]
  
  def test_get_field_value_by_name_landschl(self):
    self.assertEqual(get_field_value_by_name(self.plot_of_land_1, 'landschl'), '05')
  def test_get_field_value_by_name_gemaschl(self):
    self.assertEqual(get_field_value_by_name(self.plot_of_land_1, 'gemaschl'), '054533')
  def test_get_field_value_by_name_flstkennz(self):
    self.assertEqual(get_field_value_by_name(self.plot_of_land_1, 'flstkennz'), '05453300101559______')
    
  def test_get_field_value_by_name_flurstueckskennzeichen(self):
    self.assertEqual(get_field_value_by_name(self.plot_of_land_2, 'flurstueckskennzeichen'), '095653___05443______')
  def test_get_field_value_by_name_land(self):
    self.assertEqual(get_field_value_by_name(self.plot_of_land_2, 'land'), '09')
  def test_get_field_value_by_name_gemarkungsnummer(self):
    self.assertEqual(get_field_value_by_name(self.plot_of_land_2, 'gemarkungsnummer'), '5653')
    
  def test_get_list_of_plots_2_plots(self):
    self.assertEqual(len(get_list_of_plots(self.parsed_file_3, 'Flurstueck')), 2)
  def test_get_list_of_plots_1_plot(self):
    self.assertEqual(len(get_list_of_plots(self.parsed_file_1, 'Flurstueck')), 1)
    
    
if __name__ == '__main__':
    unittest.main()