import requests
import re
from dotenv import load_dotenv
import os

load_dotenv("secrets.env")

api_key = os.getenv('secret')
print("Your API Key is", api_key)
root_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("""What city are you in?
""")
url = f"{root_url}appid={api_key}&q={city_name}"
r = requests.get(url)
data = r.json()
if data['cod'] == 200:
    descr = data['weather'][0]['description']
    weatherid = data['weather'][0]['id']
    print(f"City Name : {city_name}")
    print(f"The Weather Condition is {descr}")
    print(f"The weather ID is {weatherid}")
else:
    print("Something Went Wrong")
fullid = weatherid
while (weatherid >= 10):
    weatherid = weatherid // 10

print("The weather type is", weatherid)
print(fullid)

if weatherid == 2:
    print("Thunder")
elif weatherid == 3:
    print("Drizzle")
elif weatherid == 5:
    print("rain")
elif weatherid == 6:
    print("snow")
elif weatherid == 7:
    print("Atmophere Condition")
elif weatherid == 8:
    print("sunny!")
else:
    print("Something went wrong and im too lazy to figure it out")