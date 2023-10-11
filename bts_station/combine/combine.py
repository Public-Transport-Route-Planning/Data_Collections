import pandas as pd
import os

# Load the first CSV file into a DataFrame
df1 = pd.read_csv("../data/mrt/blue_data.csv")

# Load the second CSV file into another DataFrame
df2 = pd.read_csv("../api/blue_lines.csv")

# Concatenate the two DataFrames
combined_df = pd.concat([df1, df2], axis=1)
combined_df = combined_df.drop(columns=["loc"])  # loc,sname

output_directory = "../data/mrt"
output_filename = "mrt_b_station.csv"
output_path = os.path.join(output_directory, output_filename)
# Save the combined DataFrame to a new CSV file
combined_df.to_csv(output_path, index=False)

# print(combined_df)
