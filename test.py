import folium
import geocoder
import pygeoip
g= geocoder.ip("37.236.252.248")

myaddress=g.latlng
print(myaddress)


m=folium.Map(location=myaddress, zoom_start=4)

folium.Marker(myaddress).add_to(m)
m.save("m.html")
print("test test")