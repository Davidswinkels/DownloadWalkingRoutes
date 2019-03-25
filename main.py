from scripts.downloader import *
import fiona
from shapely.geometry import shape
import geopandas as gpd
import matplotlib.pyplot as plt


## Constant variables
route_url = "https://download.routeyou.com/k-9aec2fc1705896b901c3ea17d6223f0a/route/5653357.gpx?language=nl"
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
filepath = "C:/Users/David/Downloads/Wandelroutes/5653357.gpx"

rows_list = []
input_rows = [1, 2, 3]
# download_to_file(route_url, default_headers, filepath)
for row in input_rows:

    layer = fiona.open(filepath, layer='tracks')
    geom = layer[0]
    route_name = geom['properties']['name']
    route_geodata = {'type': 'MultiLineString',
                     'coordinates': geom['geometry']['coordinates']}
    print(route_geodata)
    route_geometry = shape(route_geodata)
    route_dict = {'name': route_name,
                  'geometry': route_geometry}
    rows_list.append(route_dict)


print(rows_list)
routes_gdf = gpd.GeoDataFrame(rows_list)
routes_gdf.crs = {'init': 'epsg:426', 'no_defs': True}
print(routes_gdf.crs)
routes_gdf.to_crs({'init': 'epsg:28992'})
routes_gdf.plot()
plt.show()
print(routes_gdf.geometry)
print(routes_gdf.crs)



