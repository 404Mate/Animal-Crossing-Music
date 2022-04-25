# get dependancies
import asyncio
from asyncore import loop
import time
from playsound import playsound

# Get Current Time, save current hour to var
Time = time.localtime()
current_time = time.strftime("%H", Time)
hour = time.strftime("%H", Time)

#play newleaf music without weather
def noweathernewleafhourly():
    # Get Current Time, save current hour to var
    Time = time.localtime()
    current_time = time.strftime("%H", Time)
    hour = time.strftime("%H", Time)
    if hour == "00":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/12AM.mp3")
        noweathernewleafhourly()
    elif hour == "01":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/1AM.mp3")
        noweathernewleafhourly()
    elif hour == "02":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/2AM.mp3")
        noweathernewleafhourly()
    elif hour == "03":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/3AM.mp3")
        noweathernewleafhourly()
    elif hour == "04":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/4AM.mp3")
        noweathernewleafhourly()
    elif hour == "05":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/5AM.mp3")
        noweathernewleafhourly()
    elif hour == "06":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/6AM.mp3")
        noweathernewleafhourly()
    elif hour == "07":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/7AM.mp3")
        noweathernewleafhourly()
    elif hour == "08":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/8AM.mp3")
        noweathernewleafhourly()
    elif hour == "09":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/9AM.mp3")
        noweathernewleafhourly()
    elif hour == "10":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/10AM.mp3")
        noweathernewleafhourly()
    elif hour == "11":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/11AM.mp3")
        noweathernewleafhourly()
    elif hour == "12":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/12PM.mp3")
        noweathernewleafhourly()
    elif hour == "13":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/1PM.mp3")
        noweathernewleafhourly()
    elif hour == "14":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/2PM.mp3")
        print("secondloop,")
        noweathernewleafhourly()
    elif hour == "15":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/3PM.mp3")
        noweathernewleafhourly()
    elif hour == "16":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/4PM.mp3")
        noweathernewleafhourly()
    elif hour == "17":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/5PM.mp3")
        noweathernewleafhourly()
    elif hour == "18":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/6PM.mp3")
        noweathernewleafhourly()
    elif hour == "19":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/7PM.mp3")
        noweathernewleafhourly()
    elif hour == "20":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/8PM.mp3")
        noweathernewleafhourly()
    elif hour == "21":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/9PM.mp3")
        noweathernewleafhourly()
    elif hour == "22":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/10PM.mp3")
        noweathernewleafhourly()
    elif hour == "23":
        playsound("AC Music/Animal-Crossing-Music/hourly songs/11PM.mp3")
        noweathernewleafhourly()
    else:
        print("Something is wrong with detecting the time, please try again later or make a bug report")
        exit()
   
#sanity check, current hour in 24h format
print("The Hour is", hour)

#collect zipcode/skip zipcode
print("Please enter your zipcode for weather or skip to ignore")
zipcode = input("Zipcode:")
if zipcode == "skip":
    print("Ignoring weather,")
    noweathernewleafhourly()
else:
    noweathernewleafhourly()
#zip code not collected for now, no use