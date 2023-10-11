import pandas as pd

# airportlink
# csv_file = "tran-stations.csv"


# df = pd.read_csv(csv_file)


# filtered_df = df.iloc[80:88]
# columns_to_exclude = ["sid", "stype", "city", "Line", "note"]
# filtered_df = filtered_df.drop(columns=columns_to_exclude)
# filtered_df = filtered_df[::-1]

# exported_csv_file = "airportlink_lines.csv"


# filtered_df.to_csv(exported_csv_file, index=False)

# columns_to_keep = ["lon", "lat"]

# # Keep only the 'lat' and 'lon' columns
# filtered_df = filtered_df[columns_to_keep]

# # Reverse the order of columns (lon becomes lat and lat becomes lon)
# filtered_df = filtered_df.rename(columns={"lat": "lon", "lon": "lat"})

# # Specify the filename for the exported CSV file
# exported_csv = "airportlink_lines_lat_lon_reversed.csv"

# # Export the filtered DataFrame (with reversed columns) to a CSV file
# filtered_df.to_csv(exported_csv, index=False)


csv_file = "blue_lines.csv"
df = pd.read_csv(csv_file)
columns_to_keep = ["lon", "lat"]

# Keep only the 'lat' and 'lon' columns
filtered_df = df[columns_to_keep]

# Reverse the order of columns (lon becomes lat and lat becomes lon)
filtered_df = filtered_df.rename(columns={"lat": "lon", "lon": "lat"})

# Specify the filename for the exported CSV file
exported_csv = "blue_lines_reversed.csv"
filtered_df.to_csv(exported_csv, index=False)
