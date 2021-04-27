import sys
from xml.dom import minidom
import argparse
from typing import Tuple, List
import os.path

# dictionary of tag names
data_formats = {
  'aaa': ('flstkennz', 'flaeche', 'landschl', 'kreisschl', 'gmdschl', 'gemaschl'), 
  'nas': ('flurstueckskennzeichen', 'amtlicheFlaeche', 'land', 'kreis', 'gemeinde', 'gemarkungsnummer'),
}
# dictionary of 'plot of land' tag names
plot_tag_names = {
  'aaa': 'Flurstueck',
  'nas': 'AX_Flurstueck'
}
# tuple which will be used for printing field names
polish_translation_tag_names = ('numer działki', 'wielkość działki', 'numer landu', 'numer okręgu', 'numer powiatu', 'numer gemarkung')

def load_parameters() -> Tuple[str, str]:
  parser = argparse.ArgumentParser(description='Prints data about plots of land.')
  parser.add_argument('file_name', type=str, help='name of a file that will be parsed')
  parser.add_argument('file_format', type=str, help='name of the data format')
  
  arguments = parser.parse_args()
  arguments.file_format = arguments.file_format.lower()
  
  if not os.path.isfile(arguments.file_name):
    print(f"File called {arguments.file_name} does not exist.")
    sys.exit(1)
  
  
  if arguments.file_format not in data_formats:
   print(f"The {arguments.file_format} format is not supported.")
   sys.exit(1)
  
  return (arguments.file_name, arguments.file_format)

  
def parse_data(filename: str) -> minidom.Document:
  return minidom.parse(filename)


def get_list_of_plots(parsed_xml_file: minidom.Document, plot_tag_name: str) -> List[minidom.Document]:
  return parsed_xml_file.getElementsByTagName(plot_tag_name)


def get_field_value_by_name(plot_of_land: minidom.Document, tag_name: str) -> str:
  return plot_of_land.getElementsByTagName(tag_name)[0].firstChild.data


def get_display_data(parsed_xml_file: minidom.Document, file_format: str) -> List[List[str]]:
  list_of_plots = get_list_of_plots(parsed_xml_file, plot_tag_names[file_format])
  data = []
  
  for plot in list_of_plots:
    data += [ [get_field_value_by_name(plot, tag_name) for tag_name in data_formats[file_format]] ]
    
  return data


def display_data(list_of_parsed_plots_data: List[List[str]]) -> str:
  for plot_data in list_of_parsed_plots_data:
    for index, field in enumerate(plot_data):
      print(f"{polish_translation_tag_names[index].ljust(20)} {field}")
    print('---')
    


def main(): 
  file_name, file_format = load_parameters()
  parsed_file = parse_data(file_name)
  
  display_data(get_display_data(parsed_file, file_format))
  
if __name__ == "__main__":
  main()
  
  
  
  