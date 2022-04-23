from email.mime import application
import json
import sys
import folium
from matplotlib.pyplot import show

import requests


url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
data = json.loads(requests.get(f"{url}/vis1.json").text)
m = folium.Map(location=[48.218871184761596, 11.624819877497147], zoom_start=15, tiles="Stamen Terrain")

marker = folium.Marker(
    location=[48.218871184761596, 11.624819877497147],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(data, width=450, height=250)
         ),
       )

marker.add_to(m)





 

