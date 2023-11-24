import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() #Exception raised if error in response

data = response.json()["iss_position"]
latitude = data["latitude"]
longitude = data["longitude"]
t = latitude, longitude
print(t)