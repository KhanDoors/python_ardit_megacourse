import folium
import pandas as pd

data = pd.read_csv("file/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38, -100], zoom_start=5, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    fg.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            popup=str(el) + "m",
            tooltip=nm,
            radius=6,
            fill_color=color_producer(el),
            color="grey",
            fill_opacity=0.7,
        )
    )

fg.add_child(folium.GeoJson(data=(open("file/world.json", "r", encoding="utf-8-sig").read())))

map.add_child(fg)

map.save("Map1.html")
