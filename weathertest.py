# importing the required libraries
import requests
import re
api_key = "eb5432e9eecca28991f4affc8e3158c0"
root_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("""What city are you in?
""")
url = f"{root_url}appid={api_key}&q={city_name}"
r = requests.get(url)
# storing the returned json data into a variable
data = r.json()
# Checking If there is no error and the status code is 200
if data['cod'] == 200:
    descr = data['weather'][0]['description']
    weatherid = data['weather'][0]['id']
    # Displaying all the data
    print(f"City Name : {city_name}")
    print(f"The Weather Condition is {descr}")
    print(f"The weather ID is {weatherid}")
else:
    # If any error occured then print this
    print("Something Went Wrong")