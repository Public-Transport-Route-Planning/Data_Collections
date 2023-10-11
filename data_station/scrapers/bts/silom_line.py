import requests
from bs4 import BeautifulSoup
import pandas as pd

# import csv
import os
import re

url = "https://en.wikipedia.org/wiki/Silom_line"
res = requests.get(url)
res.encoding = "utf-8"
html_content = res.content
soup = BeautifulSoup(html_content, "html.parser")

table = soup.find("table", {"class": "wikitable"})

station_names_english = []
station_names_thai = []

for row in table.find_all("tr")[1:]:  # skip header table
    columns = row.find_all("td")

    if len(columns) >= 3:
        name_e = columns[1].text.strip()
        name_e = re.sub(r"\([^)]*\)", "", name_e).strip()  # clean data show only name
        name_t = columns[2].text.strip()

        station_names_thai.append(name_t)
        station_names_english.append(name_e)

data = {"name_e": station_names_english, "name_t": station_names_thai}

custom_order = ["W01"] + ["CEN_SI"] + [f"S{i:02}" for i in range(1, 13)]  # code station

data["sid"] = custom_order  # new col

df = pd.DataFrame(data)

df = df[["sid", "name_e", "name_t"]]

target_directory = "../../data/bts"  # path output result
os.makedirs(target_directory, exist_ok=True)

csv_filename = "silom_station.csv"
csv_path = os.path.join(target_directory, csv_filename)
df.to_csv(csv_path, index=False)
