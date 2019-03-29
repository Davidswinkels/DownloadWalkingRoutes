from scripts.downloader import *
import fiona
from shapely.geometry import shape
import geopandas as gpd
import matplotlib.pyplot as plt
import requests
import json
from pprint import pprint


## Constant variables
input_min_lat = 50.7
input_min_lon = 5.6
input_max_lat = 51.0
input_max_lon = 6.2


def create_bounding_boxes(min_lat, min_lon, max_lat, max_lon, rows=6, columns=12):
    


route_search_url = "https://api.routeyou.com/2.0/json/Route/k-9aec2fc1705896b901c3ea17d6223f0a/mapSearch"
route_url = "https://download.routeyou.com/k-9aec2fc1705896b901c3ea17d6223f0a/route/5907767.gpx?language=nl"
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
filepath = "C:/Users/swinkdtw/Downloads/Wandelroutes/5653357.gpx"

# Setup script
# route_search_data = '{"jsonrpc":"2.0","id":"3","method":"searchAdvanced","params":[{"bounds":{"min":{"lat":%s,"lon":%s},"max":{"lat":%s,"lon":%s}},"type.id":2,"score.min":0.5,"bounds.comparator":"geometry"},null,20,0,{"clusters":false,"addLanguage":"en","media":false,"description":false}]}' % (min_lat, min_lon, max_lat, max_lon)
# print(route_search_data)
# response = requests.post(url=route_search_url, headers=route_search_headers,
#                          data=route_search_data)
# print(response)
#
# # with open("./data/routes.txt", "wb") as file:
# #     file.write(response.content)
# #
# data = json.loads(response.content)
# pprint(data)
# print("Routes count", len(data['result']['routes']))
# print("Total routes", data['result']['total'])
# print("Taken routes", data['result']['took'])



# rows_list = []
# input_rows = [1, 2, 3]
# download_to_file(route_url, default_headers, filepath)
# for row in input_rows:
#
#     layer = fiona.open(filepath, layer='tracks')
#     geom = layer[0]
#     route_name = geom['properties']['name']
#     route_geodata = {'type': 'MultiLineString',
#                      'coordinates': geom['geometry']['coordinates']}
#     print(route_geodata)
#     route_geometry = shape(route_geodata)
#     route_dict = {'name': route_name,
#                   'geometry': route_geometry}
#     rows_list.append(route_dict)
#
#
# print(rows_list)
# routes_gdf = gpd.GeoDataFrame(rows_list)
# routes_gdf.crs = {'init': 'epsg:4326', 'no_defs': True}
# print(routes_gdf.crs)
# # routes_gdf.to_crs({'init': 'epsg:28992'})
# routes_gdf.plot()
# plt.show()
# print(routes_gdf.geometry)
# print(routes_gdf.crs)
