import pandas as pd
import os


def generate_route(stations):
    route_rows = []
    for i, (code_from, station_from, lat_from, lon_from) in enumerate(stations):
        go_row = {
            "route_id": "MRT-P",  #
            "path_type": "main",
            "direction": "go",
            "seq": i,
            "sid": code_from,
            "sname": station_from,
            "lat": lat_from,
            "lon": lon_from,
        }
        back_row = {
            "route_id": "MRT-P",  #
            "path_type": "main",
            "direction": "back",
            "seq": len(stations) - i - 1,
            "sid": code_from,
            "sname": station_from,
            "lat": lat_from,
            "lon": lon_from,
        }

        route_rows.extend([go_row, back_row])

    return route_rows


station_data_path = "../../../bts_station/data/mrt/purple_line_station.csv"

station_data = pd.read_csv(station_data_path)

stations = station_data[["sid", "name_e", "lat", "lon"]].values.tolist()

route_rows = generate_route(stations)

route_rows = pd.DataFrame(route_rows)
route_rows["direction"] = pd.Categorical(
    route_rows["direction"], categories=["go", "back"], ordered=True
)
route_rows = route_rows.sort_values(by=["direction", "seq"])


output_directory = "../../data/mrt"
output_filename = "purple_route.csv"  # html,csv

output_path = os.path.join(output_directory, output_filename)
route_rows.to_csv(output_path, index=False)
