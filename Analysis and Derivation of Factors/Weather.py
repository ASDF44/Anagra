import urllib.request
import json

def GetWeather(city_code):
	#link1= 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + ',India' + '&APPID=f447ce8f719458f1c33178bc3639edbe'
	link1= 'http://api.openweathermap.org/data/2.5/weather?id='+ str(city_code) + '&APPID=f447ce8f719458f1c33178bc3639edbe'

	x = urllib.request.urlopen(link1)
	weather = x.read()
	weather = weather.decode('ASCII')

	weather = json.loads(weather)                           #convert the json file into a dictionary datatype ==> weather
	#pass the weather information to the predict module which can predict tomorrows data


	return weather

"""#main
city_name = input("Enter your nearest city name :: ")                   # user inputs city name
#w = Weather(city_name)
weather_today = Weather.GetWeather(city_name)
for key in weather_today:
	print(key,' = ',weather_today[key])"""