# get dependancies
from sqlite3 import Time
import time
from playsound import playsound


# Get Current Time
Time = time.localtime()
current_time = time.strftime("%H", Time)


def noweathernewleafhourly():
    print("hourly music here :D")
    

hour = time.strftime("%H", Time)

print("The Hour is", hour)

print("Please enter your zipcode for weather or skip to ignore")
zipcode = input("Zipcode:")
if zipcode =="skip":
    print("Ignoring weather,")
    noweathernewleafhourly()





