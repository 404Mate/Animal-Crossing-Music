# get dependancies
import time
from playsound import playsound
import os 

# Get Current Time, save current hour to var
Time = time.localtime()
current_time = time.strftime("%H", Time)
hour = time.strftime("%H", Time)



# determine weather, pass it off to the weather specific functions
print("TESTING What do you want the weather to be?")
weather = input("""1: Sunny
2: Rainy
3: Snowy
""")
if weather == "1":
    def sunnynewleaf():
    # Get Current Time, save current hour to var and move to the songs folder
        Time = time.localtime()
        current_time = time.strftime("%H", Time)
        hour = time.strftime("%H", Time)
        if hour == "00":
                playsound("12AM.mp3")
                sunnynewleaf()()
        elif hour == "01":
                playsound("1AM.mp3")
                sunnynewleaf()()
        elif hour == "02":
                playsound("2AM.mp3")
                sunnynewleaf()()
        elif hour == "03":
                playsound("3AM.mp3")
                sunnynewleaf()()
        elif hour == "04":
                playsound("4AM.mp3")
                sunnynewleaf()()
        elif hour == "05":
                playsound("5AM.mp3")
                sunnynewleaf()()
        elif hour == "06":
                playsound("6AM.mp3")
                sunnynewleaf()()
        elif hour == "07":
                playsound("7AM.mp3")
                sunnynewleaf()()
        elif hour == "08":
                playsound("8AM.mp3")
                sunnynewleaf()()
        elif hour == "09":
                playsound("9AM.mp3")
                sunnynewleaf()()
        elif hour == "10":
                playsound("10AM.mp3")
                sunnynewleaf()()
        elif hour == "11":
                playsound("11AM.mp3")
                sunnynewleaf()()
        elif hour == "12":
                playsound("12PM.mp3")
                sunnynewleaf()()
        elif hour == "13":
                playsound("1PM.mp3")
                sunnynewleaf()()
        elif hour == "14":
                playsound("2PM.mp3")
                sunnynewleaf()()
        elif hour == "15":
                playsound("3PM.mp3")
                sunnynewleaf()()
        elif hour == "16":
                playsound("4PM.mp3")
                sunnynewleaf()()
        elif hour == "17":
                playsound("5PM.mp3")
                sunnynewleaf()()
        elif hour == "18":
                playsound("6PM.mp3")
                sunnynewleaf()()
        elif hour == "19":
                playsound("7PM.mp3")
                sunnynewleaf()()
        elif hour == "20":
                playsound("8PM.mp3")
                sunnynewleaf()()
        elif hour == "21":
                playsound("9PM.mp3")
                sunnynewleaf()()
        elif hour == "22":
                playsound("10PM.mp3")
                sunnynewleaf()()
        elif hour == "23":
                playsound("11PM.mp3")
                sunnynewleaf()()
        else:
                print("Something is wrong with detecting the time, please try again later or make a bug report")
                exit()

# play newleaf music without weather
def noweathernewleafhourly():
    # Get Current Time, save current hour to var and move to the songs folder
    Time = time.localtime()
    current_time = time.strftime("%H", Time)
    hour = time.strftime("%H", Time)
    if hour == "00":
            playsound("12AM.mp3")
            noweathernewleafhourly()
    elif hour == "01":
            playsound("1AM.mp3")
            noweathernewleafhourly()
    elif hour == "02":
            playsound("2AM.mp3")
            noweathernewleafhourly()
    elif hour == "03":
            playsound("3AM.mp3")
            noweathernewleafhourly()
    elif hour == "04":
            playsound("4AM.mp3")
            noweathernewleafhourly()
    elif hour == "05":
            playsound("5AM.mp3")
            noweathernewleafhourly()
    elif hour == "06":
            playsound("6AM.mp3")
            noweathernewleafhourly()
    elif hour == "07":
            playsound("7AM.mp3")
            noweathernewleafhourly()
    elif hour == "08":
            playsound("8AM.mp3")
            noweathernewleafhourly()
    elif hour == "09":
            playsound("9AM.mp3")
            noweathernewleafhourly()
    elif hour == "10":
            playsound("10AM.mp3")
            noweathernewleafhourly()
    elif hour == "11":
            playsound("11AM.mp3")
            noweathernewleafhourly()
    elif hour == "12":
            playsound("12PM.mp3")
            noweathernewleafhourly()
    elif hour == "13":
            playsound("1PM.mp3")
            noweathernewleafhourly()
    elif hour == "14":
            playsound("2PM.mp3")
            noweathernewleafhourly()
    elif hour == "15":
            playsound("3PM.mp3")
            noweathernewleafhourly()
    elif hour == "16":
            playsound("4PM.mp3")
            noweathernewleafhourly()
    elif hour == "17":
            playsound("5PM.mp3")
            noweathernewleafhourly()
    elif hour == "18":
            playsound("6PM.mp3")
            noweathernewleafhourly()
    elif hour == "19":
            playsound("7PM.mp3")
            noweathernewleafhourly()
    elif hour == "20":
            playsound("8PM.mp3")
            noweathernewleafhourly()
    elif hour == "21":
            playsound("9PM.mp3")
            noweathernewleafhourly()
    elif hour == "22":
            playsound("10PM.mp3")
            noweathernewleafhourly()
    elif hour == "23":
            playsound("11PM.mp3")
            noweathernewleafhourly()
    else:
            print("Something is wrong with detecting the time, please try again later or make a bug report")
            exit()
   
# sanity check, current hour in 24h format
print("The Hour is", hour)

# collect zipcode/skip zipcode
print("Please enter your zipcode for weather or skip to ignore")
zipcode = input("Zipcode:")
if zipcode == "skip":
    print("Ignoring weather,")
    os.chdir("songs")
    noweathernewleafhourly()
else:
    os.chdir("songs")
    noweathernewleafhourly()
# zip code not collected for now, no use

