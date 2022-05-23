# get dependancies
import time
from playsound import playsound
import os 
from dotenv import load_dotenv
import requests

# Load secrets, go to songs folder
load_dotenv("secrets.env")
api_key = os.getenv('apikey')
os.chdir("songs")

# Get Current Time, save current hour to var


# functions for different weathers/no weather
def updateweather():
    global weather
    root_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = zipcode
    url = f"{root_url}appid={api_key}&q={city_name}"
    r = requests.get(url)
    data = r.json()
    if data['cod'] == 200:
        descr = data['weather'][0]['description']
        weatherid = data['weather'][0]['id']
        #print(f"City Name : {city_name}")
        print(f"current weather: {descr}")
        #print(f"The weather ID is {weatherid}")
    else:
        print("Something Went Wrong")
    fullid = weatherid
    while (weatherid >= 10):
        weatherid = weatherid // 10

    #print("The weather type is", weatherid)

    if weatherid == 2:
        weather = "rainy"
    elif weatherid == 3:
        weather = "rainy"
    elif weatherid == 5:
        weather = "rainy"
    elif weatherid == 6:
        weather = "snowy"
    elif weatherid == 7:
        weather = "clear"
    elif weatherid == 8:
        weather = ""
    else:
        print("Something went wrong and im too lazy to figure it out") 
def updatetime():
    Time = time.localtime()
    current_time = time.strftime("%H", Time)
    global hour
    hour = time.strftime("%H", Time)
    hour = int(hour)
    if hour == 0:
        hour = "12AM"
    elif hour == 12:
        hour = str(hour) + "PM"
    elif hour > 12:
        hour = hour - 12
        hour = str(hour) + "PM"
    else:
        hour = str(hour) 
        hour = hour + "AM"
def clearnewleaf():
    weather = ""
    updatetime()
    song = f"{hour}{weather}.mp3"
    playsound(song)
def rainynewleaf():
    weather = "Rainy"
    updatetime()
    song = f"{hour}{weather}.mp3"
    playsound(song)
def snowynewleaf():
    weather = "Snowy"
    updatetime()
    song = f"{hour}{weather}.mp3"
    playsound(song)
def weathernewleaf():
    updateweather()
    updatetime()
    song = f"{hour}{weather}.mp3"
    playsound(song)
# sanity check, current hour in 24h format
updatetime()
print("It is now", hour)

# collect zipcode/skip zipcode
print("""How do you want weather?

1: Zipcode
2: Manual
3 Skip
4: Exit""")

weatherchoice = input()
if weatherchoice == "1":
    zipcode = input("""What is your zipcode? 
""")
    weathernewleaf()
elif weatherchoice == "2":
    manualweather = input("""
    
    
1: Sunny
2: Rainy
3: Snowy
""")
    if manualweather == "1":
        clearnewleaf()
    elif manualweather == "2":
        rainynewleaf()
    elif manualweather == "3":
        snowynewleaf()
    else:
        print("Sorry, that was not recognized")
        exit()
elif weatherchoice == "3":
    clearnewleaf()
elif weatherchoice == "4":
    print("Thank you, goodbye")
else:
    print("Sorry, that was not recognized")
    exit()