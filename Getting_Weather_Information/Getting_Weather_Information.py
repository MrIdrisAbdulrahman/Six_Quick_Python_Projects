import requests
from pprint import pprint

API_Key = '827dfc073e4d292344fb92cf7031b7b9'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)