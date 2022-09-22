# get dependancies
import time
from playsound import playsound
import os 
from dotenv import load_dotenv
import requests
from random import randint

# Load secrets, go to songs folder
load_dotenv("secrets.env")
api_key = os.getenv('apikey')
os.chdir("songs")

game = input("""
What Game do you want music from? 

1: New Horizons
2: New Leaf
3: Random

""")
if game == "1":
    game = "NH"
elif game == "2":
    game = "NL"
elif game == "3":
    game = "random"
else:
    print("Sorry, that was not recognized")
    exit()


# functions for different weathers/no weather and updating variables
def updateweather(): 
    global localweather
    root_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = f"{root_url}appid={api_key}&q={zipcode}"
    r = requests.get(url)
    data = r.json()
    if data['cod'] == 200:
        descr = data['weather'][0]['description']
        weatherid = data['weather'][0]['id']
    else:
        print("Falling back to sunny music")
        clearnewleaf()

    fullid = weatherid
    while (weatherid >= 10):
        weatherid = weatherid // 10

    #print("The weather type is", weatherid)

    if weatherid == 2:
        localweather = "rainy"
    elif weatherid == 3:
        localweather = "rainy"
    elif weatherid == 5:
        localweather = "rainy"
    elif weatherid == 6:
        localweather = "snowy"
    elif weatherid == 7:
        localweather = ""
    elif weatherid == 8:
        localweather = ""
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
    if game == "random":
        randgame = randint(1, 2)
        if randgame == 1:
            randgame = "NH"
        elif randgame == 2:
            randgame = "NL"
        playsound(f"{hour}{randgame}{weather}.mp3")
    else:
        playsound(f"{hour}{game}{weather}.mp3")
    clearnewleaf()

def rainynewleaf():
    weather = "Rainy"
    updatetime()
    if game == "random":
        randgame = randint(1, 2)
        if randgame == 1:
            randgame == "NH"
        elif randgame == 2:
            randgame == "NL"
        playsound(f"{hour}{randgame}{weather}.mp3")
    else:
        playsound(f"{hour}{game}{weather}.mp3")
    rainynewleaf()

def snowynewleaf():
    weather = "Snowy"
    updatetime()
    if game == "random":
        randgame = randint(1, 2)
        if randgame == 1:
            randgame = "NH"
        elif randgame == 2:
            randgame = "NL"
        playsound(f"{hour}{randgame}{weather}.mp3")
    else:
        playsound(f"{hour}{game}{weather}.mp3")
    snowynewleaf()

def weathernewleaf():
    global weather
    updateweather()
    updatetime()
    if game == "random":
        randgame = randint(1, 2)
        if randgame == 1:
            randgame = "NH"
        elif randgame == 2:
            randgame = "NL"
        playsound(f"{hour}{randgame}{localweather}.mp3")
    else:
        playsound(f"{hour}{game}{localweather}.mp3")
    weathernewleaf()

# sanity check, current hour in 24h format
updatetime()
print("""
It is now""", hour
)

# collect zipcode/skip zipcode
print("""
How do you want weather?

1: Zipcode
2: Manual
3 Random
4: Exit

""")

weatherchoice = input()
if weatherchoice == "1":
    zipcode = input("""
What is your zipcode or city name? 

"""
)
    updateweather()
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
    randweather = randint(1, 3)
    if randweather == 1:
        clearnewleaf()
    elif randweather == 2:
        rainynewleaf()
    else:
        snowynewleaf()
elif weatherchoice == "4":
    print("Thank you, goodbye")
else:
    print("Sorry, that was not recognized")
    exit()


#---------------------------
#  made by 404Mate with <3  
#---------------------------