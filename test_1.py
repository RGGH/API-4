import requests
from pprint import pprint

# This was deployed on GCP in 2021 - example url :
#url = "https://api-4-mmorfk42na-nw.a.run.app/ents"

# Test for localhost
url = "http://127.0.0.1:8000/ents"

params = {"features":"The Microsoft book written by Hayden Liu in 2018 was sold at $30 in America in 2019 by the Statue of liberty , it had a flower on the cover"}

answer = requests.post(url, json = params)

pprint(answer.json())