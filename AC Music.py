# get dependancies
import time
from playsound import playsound
import os 
from dotenv import load_dotenv
import requests

# Load secrets, go to songs folder
load_dotenv("secrets.env")
api_key = os.getenv('secret')
os.chdir("songs")

# Get Current Time, save current hour to var
Time = time.localtime()
current_time = time.strftime("%H", Time)
hour = time.strftime("%H", Time)

# functions for different weathers/no weather
def updateweather():
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
        rainynewleaf()
    elif weatherid == 3:
        rainynewleaf()
    elif weatherid == 5:
        rainynewleaf()
    elif weatherid == 6:
        snowynewleaf()
    elif weatherid == 7:
        sunnynewleaf()
    elif weatherid == 8:
        sunnynewleaf()
    else:
        print("Something went wrong and im too lazy to figure it out")

def sunnynewleaf():
    # Get Current Time, save current hour to var and move to the songs folder
    Time = time.localtime()
    current_time = time.strftime("%H", Time)
    hour = time.strftime("%H", Time)
    if hour == "00":
        playsound("12AM.mp3")
        sunnynewleaf()
    elif hour == "01":
        playsound("1AM.mp3")
        sunnynewleaf()
    elif hour == "02":
        playsound("2AM.mp3")
        sunnynewleaf()
    elif hour == "03":
        playsound("3AM.mp3")
        sunnynewleaf()
    elif hour == "04":
        playsound("4AM.mp3")
        sunnynewleaf()
    elif hour == "05":
        playsound("5AM.mp3")
        sunnynewleaf()
    elif hour == "06":
        playsound("6AM.mp3")
        sunnynewleaf()
    elif hour == "07":
        playsound("7AM.mp3")
        sunnynewleaf()
    elif hour == "08":
        playsound("8AM.mp3")
        sunnynewleaf()
    elif hour == "09":
        playsound("9AM.mp3")
        sunnynewleaf()
    elif hour == "10":
        playsound("10AM.mp3")
        sunnynewleaf()
    elif hour == "11":
        playsound("11AM.mp3")
        sunnynewleaf()
    elif hour == "12":
        playsound("12PM.mp3")
        sunnynewleaf()
    elif hour == "13":
        playsound("1PM.mp3")
        sunnynewleaf()
    elif hour == "14":
        playsound("2PM.mp3")
        sunnynewleaf()
    elif hour == "15":
        playsound("3PM.mp3")
        sunnynewleaf()
    elif hour == "16":
        playsound("4PM.mp3")
        sunnynewleaf()
    elif hour == "17":
        playsound("5PM.mp3")
        sunnynewleaf()
    elif hour == "18":
        playsound("6PM.mp3")
        sunnynewleaf()
    elif hour == "19":
        playsound("7PM.mp3")
        sunnynewleaf()
    elif hour == "20":
        playsound("8PM.mp3")
        sunnynewleaf()
    elif hour == "21":
        playsound("9PM.mp3")
        sunnynewleaf()
    elif hour == "22":
        playsound("10PM.mp3")
        sunnynewleaf()
    elif hour == "23":
        playsound("11PM.mp3")
        sunnynewleaf()
    else:
        print("Something is wrong with detecting the time, please try again later or make a bug report")
        exit()
def rainynewleaf():
    # Get Current Time, save current hour to var and move to the songs folder

    Time = time.localtime()
    current_time = time.strftime("%H", Time)
    hour = time.strftime("%H", Time)
    if hour == "00":
        playsound("12AMRainy.mp3")
        rainynewleaf()
    elif hour == "01":
        playsound("1AMRainy.mp3")
        rainynewleaf()
    elif hour == "02":
        playsound("2AMRainy.mp3")
        rainynewleaf()
    elif hour == "03":
        playsound("3AMRainy.mp3")
        rainynewleaf()
    elif hour == "04":
        playsound("4AMRainy.mp3")
        rainynewleaf()
    elif hour == "05":
        playsound("5AMRainy.mp3")
        rainynewleaf()
    elif hour == "06":
        playsound("6AMRainy.mp3")
        rainynewleaf()
    elif hour == "07":
        playsound("7AMRainy.mp3")
        rainynewleaf()
    elif hour == "08":
        playsound("8AMRainy.mp3")
        rainynewleaf()
    elif hour == "09":
        playsound("9AMRainy.mp3")
        rainynewleaf()
    elif hour == "10":
        playsound("10AMRainy.mp3")
        rainynewleaf()
    elif hour == "11":
        playsound("11AMRainy.mp3")
        rainynewleaf()
    elif hour == "12":
        playsound("12PMRainy.mp3")
        rainynewleaf()
    elif hour == "13":
        playsound("1PMRainy.mp3")
        rainynewleaf()
    elif hour == "14":
        playsound("2PMRainy.mp3")
        rainynewleaf()
    elif hour == "15":
        playsound("3PMRainy.mp3")
        rainynewleaf()
    elif hour == "16":
        playsound("4PMRainy.mp3")
        rainynewleaf()
    elif hour == "17":
        playsound("5PMRainy.mp3")
        rainynewleaf()
    elif hour == "18":
        playsound("6PMRainy.mp3")
        rainynewleaf()
    elif hour == "19":
        playsound("7PMRainy.mp3")
        rainynewleaf()
    elif hour == "20":
        playsound("8PMRainy.mp3")
        rainynewleaf()
    elif hour == "21":
        playsound("9PMRainy.mp3")
        rainynewleaf()
    elif hour == "22":
        playsound("10PMRainy.mp3")
        rainynewleaf()
    elif hour == "23":
        playsound("11PMRainy.mp3")
        rainynewleaf()
    else:
        print("Something is wrong with detecting the time, please try again later or make a bug report")
        exit()
def snowynewleaf():
    #Get Current Time, save current hour to var and move to the songs folder
    Time = time.localtime()
    current_time = time.strftime("%H", Time)
    hour = time.strftime("%H", Time)
    if hour == "00":
        playsound("12AMSnow.mp3")
        snowynewleaf()
    elif hour == "01":
        playsound("1AMSnow.mp3")
        snowynewleaf()
    elif hour == "02":
        playsound("2AMSnow.mp3")
        snowynewleaf()
    elif hour == "03":
        playsound("3AMSnow.mp3")
        snowynewleaf()
    elif hour == "04":
        playsound("4AMSnow.mp3")
        snowynewleaf()
    elif hour == "05":
        playsound("5AMSnow.mp3")
        snowynewleaf()
    elif hour == "06":
        playsound("6AMSnow.mp3")
        snowynewleaf()
    elif hour == "07":
        playsound("7AMSnow.mp3")
        snowynewleaf()
    elif hour == "08":
        playsound("8AMSnow.mp3")
        snowynewleaf()
    elif hour == "09":
        playsound("9AMSnow.mp3")
        snowynewleaf()
    elif hour == "10":
        playsound("10AMSnow.mp3")
        snowynewleaf()
    elif hour == "11":
        playsound("11AMSnow.mp3")
        snowynewleaf()
    elif hour == "12":
        playsound("12ONSnow.mp3")
        snowynewleaf()
    elif hour == "13":
        playsound("1ONSnow.mp3")
        snowynewleaf()
    elif hour == "14":
        playsound("2ONSnow.mp3")
        snowynewleaf()
    elif hour == "15":
        playsound("3ONSnow.mp3")
        snowynewleaf()
    elif hour == "16":
        playsound("4ONSnow.mp3")
        snowynewleaf()
    elif hour == "17":
        playsound("5ONSnow.mp3")
        snowynewleaf()
    elif hour == "18":
        playsound("6ONSnow.mp3")
        snowynewleaf()
    elif hour == "19":
        playsound("7ONSnow.mp3")
        snowynewleaf()
    elif hour == "20":
        playsound("8ONSnow.mp3")
        snowynewleaf()
    elif hour == "21":
        playsound("9ONSnow.mp3")
        snowynewleaf()
    elif hour == "22":
        playsound("10ONSnow.mp3")
        snowynewleaf()
    elif hour == "23":
        playsound("11ONSnow.mp3")
        snowynewleaf()
    else:
        print("Something is wrong with detecting the time, please try again later or make a bug report")
        exit()
def sunnynewleafweather():
    # Get Current Time, save current hour to var and move to the songs folder
    Time = time.localtime()
    current_time = time.strftime("%H", Time)
    hour = time.strftime("%H", Time)
    if hour == "00":
        playsound("12AM.mp3")
        updateweather()
    elif hour == "01":
        playsound("1AM.mp3")
        updateweather()
    elif hour == "02":
        playsound("2AM.mp3")
        updateweather()
    elif hour == "03":
        playsound("3AM.mp3")
        updateweather()
    elif hour == "04":
        playsound("4AM.mp3")
        updateweather()
    elif hour == "05":
        playsound("5AM.mp3")
        updateweather()
    elif hour == "06":
        playsound("6AM.mp3")
        updateweather()
    elif hour == "07":
        playsound("7AM.mp3")
        updateweather()
    elif hour == "08":
        playsound("8AM.mp3")
        updateweather()
    elif hour == "09":
        playsound("9AM.mp3")
        updateweather()
    elif hour == "10":
        playsound("10AM.mp3")
        updateweather()
    elif hour == "11":
        playsound("11AM.mp3")
        updateweather()
    elif hour == "12":
        playsound("12PM.mp3")
        updateweather()
    elif hour == "13":
        playsound("1PM.mp3")
        updateweather()
    elif hour == "14":
        playsound("2PM.mp3")
        updateweather()
    elif hour == "15":
        playsound("3PM.mp3")
        updateweather()
    elif hour == "16":
        playsound("4PM.mp3")
        updateweather()
    elif hour == "17":
        playsound("5PM.mp3")
        updateweather()
    elif hour == "18":
        playsound("6PM.mp3")
        updateweather()
    elif hour == "19":
        playsound("7PM.mp3")
        updateweather()
    elif hour == "20":
        playsound("8PM.mp3")
        updateweather()
    elif hour == "21":
        playsound("9PM.mp3")
        updateweather()
    elif hour == "22":
        playsound("10PM.mp3")
        updateweather()
    elif hour == "23":
        playsound("11PM.mp3")
        updateweather()
    else:
        print("Something is wrong with detecting the time, please try again later or make a bug report")
        exit()
def rainynewleafweather():
    # Get Current Time, save current hour to var and move to the songs folder

    Time = time.localtime()
    current_time = time.strftime("%H", Time)
    hour = time.strftime("%H", Time)
    if hour == "00":
        playsound("12AMRainy.mp3")
        updateweather()
    elif hour == "01":
        playsound("1AMRainy.mp3")
        updateweather()
    elif hour == "02":
        playsound("2AMRainy.mp3")
        updateweather()
    elif hour == "03":
        playsound("3AMRainy.mp3")
        updateweather()
    elif hour == "04":
        playsound("4AMRainy.mp3")
        updateweather()
    elif hour == "05":
        playsound("5AMRainy.mp3")
        updateweather()
    elif hour == "06":
        playsound("6AMRainy.mp3")
        updateweather()
    elif hour == "07":
        playsound("7AMRainy.mp3")
        updateweather()
    elif hour == "08":
        playsound("8AMRainy.mp3")
        updateweather()
    elif hour == "09":
        playsound("9AMRainy.mp3")
        updateweather()
    elif hour == "10":
        playsound("10AMRainy.mp3")
        updateweather()
    elif hour == "11":
        playsound("11AMRainy.mp3")
        updateweather()
    elif hour == "12":
        playsound("12PMRainy.mp3")
        updateweather()
    elif hour == "13":
        playsound("1PMRainy.mp3")
        updateweather()
    elif hour == "14":
        playsound("2PMRainy.mp3")
        updateweather()
    elif hour == "15":
        playsound("3PMRainy.mp3")
        updateweather()
    elif hour == "16":
        playsound("4PMRainy.mp3")
        updateweather()
    elif hour == "17":
        playsound("5PMRainy.mp3")
        updateweather()
    elif hour == "18":
        playsound("6PMRainy.mp3")
        updateweather()
    elif hour == "19":
        playsound("7PMRainy.mp3")
        updateweather()
    elif hour == "20":
        playsound("8PMRainy.mp3")
        updateweather()
    elif hour == "21":
        playsound("9PMRainy.mp3")
        updateweather()
    elif hour == "22":
        playsound("10PMRainy.mp3")
        updateweather()
    elif hour == "23":
        playsound("11PMRainy.mp3")
        updateweather()
    else:
        print("Something is wrong with detecting the time, please try again later or make a bug report")
        exit()
def snowynewleafweather():
    #Get Current Time, save current hour to var and move to the songs folder
    Time = time.localtime()
    current_time = time.strftime("%H", Time)
    hour = time.strftime("%H", Time)
    if hour == "00":
        playsound("12AMSnow.mp3")
        updateweather()
    elif hour == "01":
        playsound("1AMSnow.mp3")
        updateweather()
    elif hour == "02":
        playsound("2AMSnow.mp3")
        updateweather()
    elif hour == "03":
        playsound("3AMSnow.mp3")
        updateweather()
    elif hour == "04":
        playsound("4AMSnow.mp3")
        updateweather()
    elif hour == "05":
        playsound("5AMSnow.mp3")
        updateweather()
    elif hour == "06":
        playsound("6AMSnow.mp3")
        updateweather()
    elif hour == "07":
        playsound("7AMSnow.mp3")
        updateweather()
    elif hour == "08":
        playsound("8AMSnow.mp3")
        updateweather()
    elif hour == "09":
        playsound("9AMSnow.mp3")
        updateweather()
    elif hour == "10":
        playsound("10AMSnow.mp3")
        updateweather()
    elif hour == "11":
        playsound("11AMSnow.mp3")
        updateweather()
    elif hour == "12":
        playsound("12ONSnow.mp3")
        updateweather()
    elif hour == "13":
        playsound("1ONSnow.mp3")
        updateweather()
    elif hour == "14":
        playsound("2ONSnow.mp3")
        updateweather()
    elif hour == "15":
        playsound("3ONSnow.mp3")
        updateweather()
    elif hour == "16":
        playsound("4ONSnow.mp3")
        updateweather()
    elif hour == "17":
        playsound("5ONSnow.mp3")
        updateweather()
    elif hour == "18":
        playsound("6ONSnow.mp3")
        updateweather()
    elif hour == "19":
        playsound("7ONSnow.mp3")
        updateweather()
    elif hour == "20":
        playsound("8ONSnow.mp3")
        updateweather()
    elif hour == "21":
        playsound("9ONSnow.mp3")
        updateweather()
    elif hour == "22":
        playsound("10ONSnow.mp3")
        updateweather()
    elif hour == "23":
        playsound("11ONSnow.mp3")
        updateweather()
    else:
        print("Something is wrong with detecting the time, please try again later or make a bug report")
        exit()

# sanity check, current hour in 24h format

print("The Hour is", hour)

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
    updateweather()
elif weatherchoice == "2":
    print("""
    1: Sunny
    2: Rainy
    3: Snowy""")
    weather = input()
    if weather == "1":
        sunnynewleaf()
    elif weather == "2":
        rainynewleaf()
    elif weather == "3":
        snowynewleaf()
    else:
        print("Sorry, that was not recognized")
        exit()
elif weatherchoice == "3":
    sunnynewleaf()
elif weatherchoice == "4":
    print("Thank you, goodbye")
else:
    print("Sorry, that was not recognized")
    exit()