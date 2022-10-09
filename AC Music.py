# get dependancies
import time
from playsound import playsound
import os 
from dotenv import load_dotenv
import requests
from random import choice

# Load secrets, go to songs folder
load_dotenv("secrets.env")
api_key = os.getenv('apikey')
os.chdir("songs")

def handle_unrecognized():
    print("Sorry, that was not recognized")
    exit()

def play_song(hour, game, weather):
    # Snowy NL tracks do not include the 'y' in its filename.
    if weather == "Snowy" and game == "NL":
        weather = "Snow"

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

def get_time():
    return time.strftime("%H%p", time.localtime())

def get_game():
    return game or choice(["NH", "NL"])

def newleaf(weather=get_weather()):
    play_song(get_time(), get_game(), weather)
    newleaf(weather)

game = input("""
What Game do you want music from? 

1: New Horizons
2: New Leaf
3: Random

""")
try:
    game = ["NH", "NL", None][int(game)]   
except:
    handle_unrecognized()

# sanity check, current hour in 24h format
print("It is now", get_time())

# collect zipcode/skip zipcode
print("""
How do you want weather?

1: Zipcode
2: Manual
3: Random
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
    try:
        newleaf(["", "Rainy", "Snowy"][int(weatherchoice)])    
    except:
        handle_unrecognized()
elif weatherchoice == "3":
    newleaf(choice(["", "Rainy", "Snowy"]))
elif weatherchoice == "4":
    print("Thank you, goodbye")
else:
    handle_unrecognized()


#---------------------------
#  made by 404Mate with <3  
#---------------------------