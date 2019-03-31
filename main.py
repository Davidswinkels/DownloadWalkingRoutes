from scripts.downloader import *
import fiona
from shapely.geometry import shape
import geopandas as gpd
import matplotlib.pyplot as plt
from pprint import pprint
import requests
import json
import time
import os

# Constant variables
input_min_lat = 50.751797561
input_min_lon = 5.726110232
input_max_lat = 50.938216069
input_max_lon = 6.121604582
route_search_url = "https://api.routeyou.com/2.0/json/Route/k-9aec2fc1705896b901c3ea17d6223f0a/mapSearch"
route_search_headers = {"Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": "nl,en-US;q=0.7,en;q=0.3",
                        "Connection": "keep-alive",
                        "Content-Length": "331",
                        "Content-Type": "text/plain;charset=UTF-8",
                        "DNT": "1",
                        "Host": "api.routeyou.com",
                        "Origin": "https://www.routeyou.com",
                        "Referer": "https://www.routeyou.com/route/search/2/walking-route-search",
                        "TE": "Trailers",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"}
default_headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Accept-Language": "nl,en-US;q=0.7,en;q=0.3",
                   "Connection": "test",
                   "Cookie": "rtysid=5gf59rik6gf8o7b5an7nalcsh0; "
                             "_ga=GA1.2.1811204879.1553438381; _"
                             "gid=GA1.2.1815573989.1553438381; __"
                             "gads=ID=fab95f7aaf65227e:T=1553438384:S=ALNI_MaIjkdo1dKpYiyQKfWZEymqT7HgUQ",
                   "Host": "download.routeyou.com",
                   "Referer": "https://www.routeyou.com/nl-be/route/view/5653357/wandelroute/"
                              "in-het-spoor-van-napoleon-kasteel-reinhardstein-en-de-stuwdam-van-robertville",
                   "TE": "Trailers",
                   "Upgrade-Insecure-Requests": "1",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"}


# # Setup script
# bounding_boxes_list = create_bounding_boxes(input_min_lat, input_min_lon, input_max_lat, input_max_lon,
#                                             nr_of_rows=12, nr_of_columns=12)
# for index, bounding_box in enumerate(bounding_boxes_list):
#     route_search_data = '{"jsonrpc":"2.0","id":"3","method":"searchAdvanced","params":' \
#                         '[{"bounds":{"min":{"lat":%s,"lon":%s},"max":{"lat":%s,"lon":%s}},' \
#                         '"type.id":2,"score.min":0.5,"bounds.comparator":"geometry"},null,100,0,' \
#                         '{"clusters":false,"addLanguage":"en","media":false,"description":false}]}' \
#                         % (bounding_box['min_lat'], bounding_box['min_lon'], bounding_box['max_lat'], bounding_box['max_lon'])
#     response = requests.post(url=route_search_url, headers=route_search_headers,
#                              data=route_search_data)
#     with open("D:/Wandelroutes/Text/routes_{}.txt".format(index), "wb") as file:
#         file.write(response.content)
#     data = json.loads(response.content)
#     print("Index / routes count / total routes: ", index, "/", len(data['result']['routes']), "/", data['result']['total'])
#
#     for route in data['result']['routes']:
#         time.sleep(0.5)
#         route_url = "https://download.routeyou.com/k-9aec2fc1705896b901c3ea17d6223f0a/route/{}.gpx?language=nl".format(route['id'])
#         filepath = "D:/Wandelroutes/GPX/{}.gpx".format(route['id'])
#         download_to_file(route_url, default_headers, filepath)

dir_filepath = "D:/Wandelroutes/GPX"
filenames = os.listdir(dir_filepath)
rows_list = []
for filename in filenames:
    layer = fiona.open(os.path.join(dir_filepath, filename), layer='tracks')
    geom = layer[0]
    route_name = geom['properties']['name']
    route_geodata = {'type': 'MultiLineString',
                     'coordinates': geom['geometry']['coordinates']}
    route_geometry = shape(route_geodata)
    route_id = os.path.splitext(os.path.basename(filename))[0]
    route_dict = {'id': str(route_id),
                  'name': route_name,
                  'url': "https://www.routeyou.com/nl-nl/route/view/" + str(route_id),
                  'geometry': route_geometry}
    rows_list.append(route_dict)

routes_gdf = gpd.GeoDataFrame(rows_list)
routes_gdf.crs = {'init': 'epsg:4326', 'no_defs': True}
routes_gdf.to_file("D:/Wandelroutes/walking_routes.shp")
