from folium import Map, Marker, LatLngPopup, plugins
import os

from MAC_DictionaryList import latitude_list, longitude_list,max_lat, min_lat, max_long, min_long
from MAC_Variables import base_location, start_lat, start_long, popup_objects, icon_objects

def generate_map(lat, long):
    return Map([lat, long], template = 'template.html')


def add_layers(latitude, longitude, popup_object, icon_object):
    base_map.add_child(Marker([latitude, longitude], popup=popup_object, icon=icon_object))
    return base_map


def position_marker(map_layer):
    return map_layer.add_child(LatLngPopup())


def mini_map(map_name):
    minimap = plugins.MiniMap()
    map_name.add_child(minimap)


def find_home(map_name):
    plugins.LocateControl().add_to(map_name)
    plugins.Geocoder().add_to(map_name)


def fit_bounds(map_name):
    map_name.fit_bounds([[min_lat, min_long], [max_lat, max_long]])
    map_name.add_child(plugins.MeasureControl())
def save_map(html_name):
    os.chdir(base_location)
    base_map.save(html_name)


if __name__ == '__main__':
    base_map = generate_map(start_lat, start_long)

    for lat, long, popup, icon in zip(latitude_list, longitude_list, popup_objects, icon_objects):
        add_layers(lat, long, popup, icon)
    position_marker(base_map)
    mini_map(base_map)
    find_home(base_map)
    fit_bounds(base_map)
    save_map('MAC_Locations_2.html')