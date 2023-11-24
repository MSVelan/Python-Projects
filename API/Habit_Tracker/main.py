import requests, datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "msvelan"
TOKEN = "jkweurhvnhdlkgvldafgu123"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

GRAPH_ID = graph_config['id']
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.date.today()
today = today.strftime("%Y%m%d")

yesterday = datetime.datetime(year=2023, day=11, month=6)
yesterday = yesterday.strftime("%Y%m%d")
# print(yesterday)

pixel_data = {
    "date": yesterday,
    "quantity": "8.3"
}

# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

updateToday = {
    "quantity": "6.4"
}
# response = requests.put(url=f"{pixel_endpoint}/{today}",json=updateToday,headers=headers)
# print(response.text)

response = requests.delete(url=f"{pixel_endpoint}/{yesterday}", headers=headers)
print(response.text)