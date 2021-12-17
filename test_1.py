import requests

url = "https://api-4-mmorfk42na-nw.a.run.app/ents"
#url = "http://127.0.0.1:8000/ents"

params = {"features":"The book written by Hayden Liu in 2018 was sold at $30 in America in 2019"}

answer = requests.post(url, json = params)

print(answer.text)