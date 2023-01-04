import time
import playsound
import os 
import dotenv 
import requests
import random
import sys

global apikey
global weather
global location



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
    return hour



def main():
    dotenv.load_dotenv("secrets.env")
    apikey = os.getenv('apikey')
    os.chdir("songs")
    print("\nWelcome to Animal Crossing Music, made with <3 by 404Mate!")
    if apikey == None:
        print("\nWARNING! No API key detected. Local weather will not work")

    try:
        while True:
            game = input("""
    What game do you want music from?
    1: New Horizons
    2: New Leaf
    3: Random
""")
            if game != "1" and game != "2" and game != "3":
                print("Sorry, that was not recognized")
            else:
                break
        while True:
            weather = input("""
    How do you want weather?
    1: Zipcode/City
    2: Manual
    3: Random
""")
            if weather != "1" and weather != "2" and weather != "3":
                print("Sorry, that was not recognized")
            else:
                break
        match game: 
            case "1":
                game = "NH"  
            case "2":
                game = "NL"
            case "3":
                game = random.choice(["NH", "NL"])

        match weather: 
            case "1":
                location = input("\nWhat is your zipcode or city name?\n")
                os.system('cls' if os.name == 'nt' else 'clear')
                while True:
                    root_url = "http://api.openweathermap.org/data/2.5/weather?"
                    url = f"{root_url}appid={apikey}&q={location}"
                    r = requests.get(url)
                    data = r.json()
                    if data['cod'] == 200:
                        descr = data['weather'][0]['description']
                        weatherid = data['weather'][0]['id']
                    else:
                        print("\n Sorry, your location was not recognized or you lost internet connection")
                    
                    while (weatherid >= 10):
                        weatherid //= 10
                    match weatherid:
                        case 2:
                            weather = "Rainy"
                        case 3: 
                            weather = "Rainy"
                        case 5:
                            weather = "Rainy"
                        case 6:
                            weather = "Snowy"
                        case 7:
                            weather = ""
                        case 8:
                            weather = ""
                    playsound.playsound(f"{updatetime()}{game}{weather}.mp3")


            case "2":
                while True:
                    weather = input("""
    What weather do you want?
    1: Sunny
    2: Rainy
    3: Snowy
""")                
                    if weather != "1" and weather != "2" and weather != "3":
                        print("Sorry, that was not recognized")
                    else: 
                        break
                os.system('cls' if os.name == 'nt' else 'clear')
                match weather:
                    case "1":
                        weather = ""
                    case "2":
                        weather = "Rainy"
                    case "3":
                        weather = "Snowy"

                while True:
                    playsound.playsound(f"{updatetime()}{game}{weather}.mp3")

            case "3":
                    weather = random.choice(["", "Rainy", "Snowy"])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    while True:
                        playsound.playsound(f"{updatetime()}{game}{weather}.mp3")


        
    except:
        print("\nGoodbye!\n")



if __name__ == "__main__":
    main()

#---------------------------
#  made by 404Mate with <3  
#---------------------------
