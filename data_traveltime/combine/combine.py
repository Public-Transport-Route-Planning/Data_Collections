import pandas as pd


# Load the first CSV file into a DataFrame
df1 = pd.read_csv("../scripts/mrt/pi_go.csv")

# Load the second CSV file into another DataFrame
df2 = pd.read_csv("../scripts/mrt/pi_back.csv")

# Concatenate the two DataFrames
combined_df = pd.concat([df1, df2], axis=0)
# combined_df = combined_df.drop(columns=["loc"])  # loc,sname

combined_df.to_csv("../data/mrt/mrt_pi_time.csv", index=False)
