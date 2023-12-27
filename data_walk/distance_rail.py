import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist

bus_stop = (
    "https://raw.githubusercontent.com/SiwakornJew/dataforwork/main/busstops-dat.csv"
)
bstops = pd.read_csv(bus_stop)
bstops_dist = bstops[["lat", "lon"]].to_numpy()

rstops = pd.read_csv("../data_station/data/rail_station.csv")
rstops_dist = rstops[["lat", "lon"]].to_numpy()
# rstops.to_csv("./rail/test.csv", index=False)

distances = cdist(bstops_dist, rstops_dist, metric="euclidean") * 111000
walking_dist = 500
matched_stops = []
for i in range(len(bstops)):
    for j in range(len(rstops)):
        if distances[i, j] <= walking_dist:
            matched_stops.append(
                (bstops.iloc[i]["stopid"], rstops.iloc[j]["stopid"], distances[i, j])
            )
results_df = pd.DataFrame(matched_stops, columns=["sid1", "sid2", "dist_m"])
results_df["dist_m"] = results_df["dist_m"].apply(lambda x: format(x, ".2f"))

results_df.to_csv("./data/dist_rail.csv", index=False)
