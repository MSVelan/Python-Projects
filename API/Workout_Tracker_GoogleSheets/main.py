import requests, datetime, os
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}

workout_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

s = input("Enter what workout did you do? ")

workout_Data = {
    "query": s,
    "gender": "male",
    "weight_kg": 73,
    "height_cm": 187,
    "age": 19
}

workoutRes = requests.post(url=workout_ENDPOINT, json=workout_Data, headers= headers)
data = workoutRes.json()



sheety_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
authToken = os.environ.get("SECRET")

for i in range(len(data['exercises'])):
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    sheetPayload = {
        "workout":{
            "date":date,
            "time": time,
            "exercise": data['exercises'][i]['name'].title(),
            "duration": data['exercises'][i]['duration_min'],
            "calories": data['exercises'][i]['nf_calories']
        }
    }

    sheetHeaders = {
        "Content-Type": "application/json",
        "Authorization": authToken
    }
    sheetPostRes = requests.post(url=sheety_ENDPOINT, json=sheetPayload, headers=sheetHeaders)
    print(sheetPostRes.text)
    
    