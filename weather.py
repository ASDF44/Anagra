import urllib.request
import json

def GetWeather(city_code):
	#link1= 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + ',India' + '&APPID=f447ce8f719458f1c33178bc3639edbe'
	link1= 'http://api.openweathermap.org/data/2.5/weather?id='+ city_code + '&APPID=f447ce8f719458f1c33178bc3639edbe'
	print(link1)

	x = urllib.request.urlopen(link1)
#	print('0')
	weather = x.read()
#	print('1')
#	weather = weather.decode('ASCII')
#	print('2')
	weather = json.loads(weather)                           #convert the json file into a dictionary datatype ==> weather
	#pass the weather information to the predict module which can predict tomorrows data
#	print('3')
#	print(weather)
	return weather

"""#main
city_name = input("Enter your nearest city name :: ")                   # user inputs city name
#w = Weather(city_name)
weather_today = Weather.GetWeather(city_name)
for key in weather_today:
	print(key,' = ',weather_today[key])"""


#print(GetWeather(1254661))