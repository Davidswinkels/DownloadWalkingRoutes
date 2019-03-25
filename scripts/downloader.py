import requests
import geopandas as gpd

def store_bytes_to_filepath(content, filepath):
    with open(filepath, 'wb') as file:
        file.write(content)


def download_to_file(url, headers, filepath):
    content = download_content(url, headers)
    store_bytes_to_filepath(content, filepath)


def download_content(url, headers):
    response = requests.get(url, headers=headers)
    return response.content


def read_gpx_to_geodataframe(input_filepath):
    input_gdf = gpd.read_file(input_filepath)
    return input_gdf
