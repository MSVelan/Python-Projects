import requests, geocoder
from datetime import datetime

timenow = datetime.now()
g=geocoder.ip('me')

parameters = {
    'lat':g.latlng[0],
    'lng':g.latlng[1],
    'formatted':0
}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

# print(timenow)
# print(sunrise)

l = sunrise.split("T")
sunrisetime = l[1].split(":")

l = sunset.split("T")
sunsettime = l[1].split(":")
print(sunrisetime[0],timenow.hour)