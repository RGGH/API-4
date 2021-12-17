import requests

#url = "https://neuro-2fle3wxkia-nw.a.run.app/vars"
url = "http://127.0.0.1:8000/ents"

params = {"features":"The book written by Hayden Liu in 2018 was sold at $30 in America in 2019"}

answer = requests.post(url, json = params)

print(answer.text)