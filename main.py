import requests

url = "https://community-open-weather-map.p.rapidapi.com/forecast"

querystring = {"q":"san francisco,us"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "5f45b4b2f9msh70a2f9ff2fdaf61p160266jsn303646720889"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)