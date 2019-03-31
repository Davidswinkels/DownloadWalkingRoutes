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


def create_bounding_boxes(min_lat, min_lon, max_lat, max_lon, nr_of_rows=6, nr_of_columns=12):
    bounding_boxes_list = []
    delta_lat = max_lat - min_lat
    delta_lon = max_lon - min_lon
    dist_lat = delta_lat / nr_of_rows
    dist_lon = delta_lon / nr_of_columns
    for row_nr in range(nr_of_rows):
        for column_nr in range(nr_of_columns):
            min_lat_window = min_lat + (dist_lat * row_nr)
            min_lon_window = min_lon + (dist_lon * column_nr)
            max_lat_window = min_lat + (dist_lat * (row_nr + 1))
            max_lon_window = min_lon + (dist_lon * (column_nr + 1))
            bounding_box_dict = {"min_lat": min_lat_window,
                                 "min_lon": min_lon_window,
                                 "max_lat": max_lat_window,
                                 "max_lon": max_lon_window}
            bounding_boxes_list.append(bounding_box_dict)
    return bounding_boxes_list
