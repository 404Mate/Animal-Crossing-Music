import dotenv
import os
import time

dotenv.load_dotenv("secrets.envg")
apikey = os.getenv('apikey')


print(apikey)


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
print(hour)