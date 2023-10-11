import pandas as pd
import folium
import random

# arl = pd.read_csv("../data/airportlink/arl_p.csv")
# bts_g = pd.read_csv("../data/bts/bts_g_p.csv")
# bts_si = pd.read_csv("../data/bts/bts_si_p.csv")
# bts_su = pd.read_csv("../data/bts/bts_su_p.csv")
# mrt_b = pd.read_csv("../data/mrt/mrt_b_p.csv")
# mrt_p = pd.read_csv("../data/mrt/mrt_p_p.csv")
# mrt_y = pd.read_csv("../data/mrt/mrt_y_p.csv")

# m = folium.Map(location=[13.726478, 100.509032], zoom_start=14)


# def plot_polyline(df, color, weight):
#     # Check if the 'lat' and 'lon' columns exist in the DataFrame
#     if "lat" in df.columns and "lon" in df.columns:
#         # Create a Folium map
#         m = folium.Map(location=[13.726478, 100.509032], zoom_start=14)

#         # Extract coordinates from the DataFrame
#         coordinates = df[["lat", "lon"]].values.tolist()

#         # Create a polyline using the coordinates
#         folium.PolyLine(
#             locations=coordinates,
#             color=color,
#             weight=weight,
#         ).add_to(m)

#         # Save the map to an HTML file
#         map_filename = f"{color}_map.html"
#         m.save(map_filename)
#         print(f"Map with color {color} saved as {map_filename}")
#     else:
#         print(f"'lat' and 'lon' columns not found in the DataFrame for color {color}")


# # Add polylines for each line
# plot_polyline(arl, "red", 5)
# plot_polyline(bts_g, "blue", 5)
# plot_polyline(bts_si, "green", 5)
# plot_polyline(bts_su, "orange", 5)
# plot_polyline(mrt_b, "purple", 5)
# plot_polyline(mrt_p, "pink", 5)
# plot_polyline(mrt_y, "yellow", 5)

# # Save the map to an HTML file
# m.save("transit_map.html")

df = pd.read_csv("../data/combine/polyline.csv")
f = folium.Figure(width=800, height=400)

m = folium.Map(
    width="100%",
    height="100%",
    tiles="cartodbpositron",
    location=(13.771005, 100.621933),
    zoom_start=13,
).add_to(f)

for index, row in df.iterrows():
    route_id = row["route_id"]
    path_type = row["path_type"]
    direction = row["direction"]
    rpath = eval(row["polyline"])

    if (path_type == "main") and (direction == "go"):
        color = "#" + "%06x" % random.randint(0, 0xFFFFFF)
        folium.PolyLine(
            rpath, color=color, weight=5, opacity=0.5, popup=path_type
        ).add_to(m)
m.save("transit_map.html")
