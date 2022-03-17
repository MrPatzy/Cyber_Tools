from contextlib import nullcontext
import requests

API_KEY = "89cb9120c3fcc2d343a82a8d7141fc5d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    

def temp_conv(T, M):
    if (M == "C"):
        return round(T - 273.15, 2)
    elif (M == "F"):
        return round( ( ( (T - 273.15) * (9 / 5) ) + 32 ), 2)
    else:
        return T

city = input("Enter a city name: ")
print
wanted_temp = input("What temperature would you like? \n[F]arenheight, [C]elsius or [K]elvin? ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #print(data)
    weather = data['weather'][0]['description']
    print(weather + "y")
    temperature = round(data["main"]["temp"])
    feel_temp = round(data["main"]["feels_like"])
    print("The weather in ", city , "is ", weather) 
    print("The temperature is,",temp_conv(temperature, wanted_temp)," but it feels like", temp_conv(feel_temp, wanted_temp))
else:
    print("An error occured.")