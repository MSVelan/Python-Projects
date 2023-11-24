import requests
apiKey = "Xp2GhMHPlUoV6WycD4yrV4dOjTHMLYcC"
endpoint = "https://tequila-api.kiwi.com"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
        
    def getIataCode(self, city):
        locationEndpoint = f"{endpoint}/locations/query"
        parameters = {
            "term":  city,
            "location_types": "city",
            "limit": 10
        }
        headers = {
            "apikey":apiKey
        }
        response = requests.get(url=locationEndpoint,headers=headers, params=parameters)
        results = response.json()["locations"]
        iatacode = results[0]["code"]
        return iatacode