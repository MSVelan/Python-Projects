import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
url = "https://opentdb.com/api.php"

parameters = {
    "amount":10,
    "type":'boolean'
}

response = session.get(url,params=parameters)
response.raise_for_status()
data = response.json()
questionData = data["results"]