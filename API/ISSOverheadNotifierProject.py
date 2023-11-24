import requests,geocoder,smtplib,time
from datetime import datetime

myEmail = "muthiahsivavelan2026@gmail.com"
password = "knuhubbiochxgtvk"

g = geocoder.ip('me')
myLat = g.latlng[0]
myLong = g.latlng[1]

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()["iss_position"]
issLatitude = float(data["latitude"])
issLongitude = float(data["longitude"])

parameters={
    "lat":myLat,
    "lng":myLong,
    "formatted":0
}

sunresponse = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
sunresponse.raise_for_status()

data = sunresponse.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

timenow = datetime.now()

connection = smtplib.SMTP("smtp.gmail.com:587")
connection.starttls()
connection.login(myEmail,password=password)

while(True):
    if(abs(myLat-issLatitude)<=5 and abs(myLong-issLongitude)<=5 and (timenow.hour>=sunset or timenow.hour<=sunrise)):
        connection.sendmail(from_addr=myEmail,to_addrs="muthiahsvn@gmail.com",msg="Subject:ISS is nearby and right time to watch it\n\nTake a look at the sky and you might be able to watch the International Space Satellite.. \n It is in the close proximity and would be in the visible range. It would be a great sight to view at night.. Have fun watching!!")
    time.sleep(60)
    
connection.close()