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


def play_song(hour, game, weather):
    playsound(f"{hour}{game}{weather}.mp3")

# functions for different weathers/no weather and updating variables
def get_weather(): 
    root_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = f"{root_url}appid={api_key}&q={zipcode}"
    r = requests.get(url)
    data = r.json()
    if data['cod'] == 200:
        weatherid = data['weather'][0]['id']
    else:
        print("Falling back to sunny music")
        newleaf("")

    while (weatherid >= 10):
        weatherid = weatherid // 10

    # https://openweathermap.org/weather-conditions
    if weatherid == 2:
        localweather = "rainy"
    elif weatherid == 3:
        localweather = "rainy"
    elif weatherid == 5:
        localweather = "rainy"
    elif weatherid == 6:
        localweather = "snowy"
    else:
        localweather = ""

    return localweather

def updatetime():
    global hour
    hour = time.strftime("%H%p", time.localtime())

def newleaf(weather=get_weather()):
    updatetime()
    if game == "random":
        randgame = randint(1, 2)
        if randgame == 1:
            randgame = "NH"
        elif randgame == 2:
            randgame = "NL"
        play_song(hour, randgame, weather)
    else:
        play_song(hour, game, weather)
    newleaf(weather)

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
    newleaf()
elif weatherchoice == "2":
    manualweather = input("""
1: Sunny
2: Rainy
3: Snowy

""")
    if manualweather == "1":
        newleaf("")
    elif manualweather == "2":
        newleaf("Rainy")
    elif manualweather == "3":
        newleaf("Snow")
    else:
        print("Sorry, that was not recognized")
        exit()
elif weatherchoice == "3":
    randweather = randint(1, 3)
    if randweather == 1:
        newleaf("")
    elif randweather == 2:
        newleaf("Rainy")
    else:
        newleaf("Snow")
elif weatherchoice == "4":
    print("Thank you, goodbye")
else:
    print("Sorry, that was not recognized")
    exit()


#---------------------------
#  made by 404Mate with <3  
#---------------------------