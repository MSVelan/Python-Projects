import datetime
import requests 
from pprint import pprint

now = datetime.datetime.now()
days = 6*30

today = now.strftime("%d/%m/%Y")

till = now + datetime.timedelta(days=days)
finalDate = till.strftime("%d/%m/%Y")

apiKey = "Xp2GhMHPlUoV6WycD4yrV4dOjTHMLYcC"
endpoint = "https://tequila-api.kiwi.com"

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, sheetdata, to) -> None:
        self.sheetdata = sheetdata
        self.flyFrom = "DEL"
        self.flyTo = to
        self.dateFrom = today
        self.dateTo = finalDate
        self.minStay = 7
        self.maxStay = 28
        self.flightType = "round"
        self.adults = 1
        self.selectedCabins = "M"
        self.curr = "INR"
        self.locale = "en"
        for row in sheetdata:
            if(row['iataCode']==to):
                self.lowestPrice = row['lowestPrice']
    def getPrice(self):
        parameters = {
            "fly_from": self.flyFrom,
            "fly_to": self.flyTo,
            "date_from": self.dateFrom,
            "date_to": self.dateTo,
            "nights_in_dst_from": self.minStay,
            "nights_in_dst_to": self.maxStay,
            "flight_type": self.flightType,
            "adults": self.adults,
            "selected_cabins": self.selectedCabins,
            "curr": self.curr,
            "locale": self.locale
        }

        headers = {
            "apikey": apiKey
        }

        response = requests.get(url=f"{endpoint}/v2/search", headers=headers, params=parameters)
        data = response.json()
        flights = []
        for i in data["data"]:
            if(int(i['price'])<self.lowestPrice):
                flights.append(i)
        # pprint(flights)
        # print(type(data))

        minflight = None
        minPrice = self.lowestPrice
        for flight in flights:
            if(flight['price']<minPrice):
                minflight = flight
                minPrice = flight['price']
        
        return minPrice