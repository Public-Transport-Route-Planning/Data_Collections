import pandas as pd
import os

arl = pd.read_csv("../data/airportlink/arl_p.csv")
bts_g = pd.read_csv("../data/bts/bts_g_p.csv")
bts_si = pd.read_csv("../data/bts/bts_si_p.csv")
bts_su = pd.read_csv("../data/bts/bts_su_p.csv")
mrt_b = pd.read_csv("../data/mrt/mrt_b_p.csv")
mrt_p = pd.read_csv("../data/mrt/mrt_p_p.csv")
mrt_y = pd.read_csv("../data/mrt/mrt_y_p.csv")

# Concatenate the two DataFrames
combined_df = pd.concat([arl, bts_g, bts_si, bts_su, mrt_b, mrt_p, mrt_y], axis=0)
# combined_df = combined_df.drop(columns=["loc"])  # loc,sname

output_directory = "../data/combine"
output_filename = "polyline.csv"
output_path = os.path.join(output_directory, output_filename)
# Save the combined DataFrame to a new CSV file
combined_df.to_csv(output_path, index=False)
