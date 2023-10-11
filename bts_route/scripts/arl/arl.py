import pandas as pd

route_id = "ARL"
path_type = "main"
directions = ["go", "back"]
coordinates = [
    (13.698087, 100.7522355),
    (13.7159514, 100.7570186),
    (13.7178609, 100.757585),
    (13.7196536, 100.758306),
    (13.7224135, 100.7596536),
    (13.7241729, 100.7601986),
    (13.7259718, 100.7603467),
    (13.726396, 100.7603198),
    (13.7267493, 100.7602276),
    (13.7270276, 100.7601106),
    (13.7271704, 100.760013),
    (13.72731, 100.7599111),
    (13.727679, 100.7594175),
    (13.7278833, 100.7588725),
    (13.727734, 100.7486244),
    (13.7274872, 100.741127),
    (13.7280792, 100.7344322),
    (13.7296967, 100.7200727),
    (13.732844, 100.6914572),
    (13.7379576, 100.6453466),
    (13.7429528, 100.6003118),
    (13.7435236, 100.5955271),
    (13.7439373, 100.5918696),
    (13.7443104, 100.5902485),
    (13.7465135, 100.5803361),
    (13.748702, 100.5707145),
    (13.7497588, 100.5657492),
    (13.750087, 100.5645314),
    (13.7505279, 100.563377),
    (13.7510597, 100.5611013),
    (13.7515794, 100.5587829),
    (13.7518941, 100.5565878),
    (13.7528414, 100.5524025),
    (13.7551378, 100.5418289),
    (13.7567131, 100.5349773),
]
columns = ["route_id", "path_type", "direction", "polyline"]
dfs = []

for direction in directions:
    if direction == "back":
        # Create a new list of coordinates with the last set at the front
        reversed_coordinates = coordinates[::-1]
        data = [(route_id, path_type, direction, reversed_coordinates)]
    else:
        data = [(route_id, path_type, direction, coordinates)]

    df = pd.DataFrame(data, columns=columns)
    dfs.append(df)

# Combine DataFrames
result_df = pd.concat(dfs, ignore_index=True)

# Save to CSV
result_df.to_csv("airportlink_route.csv", index=False)
