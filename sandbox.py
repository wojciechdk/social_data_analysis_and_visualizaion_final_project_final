#%%
import json

# Load the geo shapes from the json file.
with open('resources/data/raw/geo/SFPD_district_shapes.geojson') as json_file:
    district_geo_shapes2 = json.load(json_file)

with open('resources/data/raw/geo/bydele.geojson',
          encoding='windows-1252'
          ) as json_file:
    district_geo_shapes = json.load(json_file)

district_names = ['Nørrebro', 'Brønshøj-Husum', 'Bispebjerg',
                  'Amager Vest', 'Vanløse', 'Indre By', 'Amager Øst',
                  'Østerbro', 'Vesterbro/Kongens Enghave', 'Valby']

for idx, district_name in enumerate(district_names):
    district_geo_shapes['features'][idx]['id'] = district_name
    district_geo_shapes['features'][0]['properties']['District'] = district_name

