#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


flight=FlightSearch()
for row in sheet_data:
    if(row['iataCode']==''):
        row['iataCode'] = flight.getIataCode(row['city'])
    
# pprint(sheet_data)

data_manager.destination_data = sheet_data

# pprint(sheet_data)

for row in sheet_data:
    flightdata = FlightData(sheet_data, row['iataCode'])
    price = flightdata.getPrice()
    if(price<row['lowestPrice']):
        row['lowestPrice'] = price

data_manager.update_destination_codes()