import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import os
import re

url = "https://en.wikipedia.org/wiki/Pink_Line_(Bangkok)"
res = requests.get(url)
res.encoding = "utf-8"
html_content = res.content
soup = BeautifulSoup(html_content, "html.parser")

tables = soup.find_all("table", {"class": "wikitable"})

station_names_english = []
station_names_thai = []


for table in tables:
    for row in table.find_all("tr")[1:]:  # skip header table
        columns = row.find_all("td")

        if len(columns) >= 3:
            name_e = columns[1].text.strip()
            name_e = re.sub(
                r"\([^)]*\)", "", name_e
            ).strip()  # clean data show only name
            name_t = columns[2].text.strip()

            station_names_thai.append(name_t)
            station_names_english.append(name_e)


# num_stations = len(station_names_english)
# station_codes = [f'BL{i+1}' for i in range(num_stations)]

data = {
    # 'code': station_codes,
    "name_e": station_names_english,
    "name_t": station_names_thai,
}

df = pd.DataFrame(data)

rows_to_drop = list(range(30, 33))
df = df[~df.index.isin(rows_to_drop)]

custom_order = [f"PK{i:02}" for i in range(1, len(df) + 1)]  # code station
df["sid"] = custom_order  # new col

df = df[["sid", "name_e", "name_t"]]


target_directory = "../../data/mrt"  # path output result
os.makedirs(target_directory, exist_ok=True)

csv_filename = "pink_data.csv"
csv_path = os.path.join(target_directory, csv_filename)
df.to_csv(csv_path, index=False)
