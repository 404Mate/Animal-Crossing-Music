# get dependancies
import time
from playsound import playsound
import os 
os.chdir("songs")

# Get Current Time, save current hour to var
Time = time.localtime()
current_time = time.strftime("%H", Time)
hour = time.strftime("%H", Time)

# functions for different weathers/no weather
def updateweather():
    if weather == "1":
        sunnynewleaf()
    elif weather == "2":
        rainynewleaf()
    elif weather == "3":
        snowynewleaf()
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
    print("This is not yet available")
    exit()
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
    noweathernewleafhourly()
elif weatherchoice == "4":
    print("Thank you, goodbye")
else:
    print("Sorry, that was not recognized")
    exit()