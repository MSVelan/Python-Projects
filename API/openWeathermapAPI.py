import requests,geocoder

g = geocoder.ip('me')

lat,long = g.latlng

apiKey = "f37bfa0188304bac1776338eb4bc3132"

parameters={
    "lat":lat,
    "lon":long,
    "api":apiKey
}
url = "https://api.openweathermap.org/data/3.0/onecall"

print(lat,long)
# response = requests.get(url=url,params=parameters)
# print(response.status_code)

