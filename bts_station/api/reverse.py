import requests

api_key = "AIzaSyCtmL7XR_iyRJ5nODJCZDUAco_wqs5BzCY"

latitude = 13.807000
longitude = 100.574789
# 13.696771, 100.605323
# 13.6611434, 100.6017937
# 13.661143, 100.601794
# 13.592076, 100.608952
# 13.592079, 100.608906
# 13.584324, 100.608027
# 13.8752°N 100.5967°E
# 13.721117, 100.503695
# 13.875799, 100.433772
# 13.797711, 100.547576
13.806088, 100.573642
url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"

response = requests.get(url)
data = response.json()

if data["status"] == "OK":
    formatted_address = data["results"][0]["formatted_address"]
    print(f"Formatted Address: {formatted_address}")
else:
    print("Error in retrieving data")
