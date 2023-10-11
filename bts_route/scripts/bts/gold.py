import pandas as pd

route_id = "BTS-G"
path_type = "main"
directions = ["go", "back"]
coordinates = [
    (13.721103, 100.503684),
    (13.7210666, 100.5056127),
    (13.7210861, 100.5056838),
    (13.7211196, 100.5057508),
    (13.7211647, 100.5058031),
    (13.7212093, 100.5058481),
    (13.7213495, 100.5059185),
    (13.721481, 100.5059804),
    (13.7216199, 100.5060464),
    (13.7217345, 100.5061328),
    (13.7218301, 100.5062835),
    (13.7218596, 100.5063694),
    (13.7218658, 100.5064611),
    (13.7218635, 100.5065627),
    (13.7218466, 100.5066633),
    (13.7216959, 100.5074852),
    (13.7214588, 100.5085178),
    (13.7214437, 100.5086122),
    (13.7214569, 100.5086938),
    (13.7214676, 100.5087356),
    (13.7214854, 100.5087694),
    (13.7215292, 100.5088332),
    (13.7215881, 100.5088938),
    (13.7216923, 100.508955),
    (13.7249358, 100.5091803),
    (13.726478, 100.509032),
    (13.7290026, 100.5088096),
    (13.7295133, 100.5087603),
    (13.7296553, 100.5087522),
    (13.7297806, 100.5087195),
    (13.7298896, 100.5086643),
    (13.7299912, 100.5085763),
    (13.7300732, 100.508458),
    (13.730379, 100.507646),
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
result_df.to_csv("bts_g_p.csv", index=False)
