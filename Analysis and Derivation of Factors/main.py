import Weather                # import the custom Weather module
import Database
from flask import Flask, render_template

class Database1:
    def __init__(self, city_name):
        self.city_name = city_name

    def GetCode(self):
        return Database.GetData(city_name)


class Weather1:
    def __init__(self, city_code1):
        self.city_code = city_code1
    def Forecast(self):
        return Weather.GetWeather(city_code1)     # get weather data

class ncbi:
    def __init__(self,crop):
        self.crop = crop
    def getncbi(crop):
        return fasta.GetNCBI(crop)







while(1):
    city_name = str(input("Enter the city's name: "))

    # access city code by the city name
    cc = Database1(city_name)                 # use of Database1 class
    city_code1 = cc.GetCode()                  # Get the city_code from the table city_codes using city name
    print('city code = ',city_code1)

    if  city_code1 == None:
        print('City unavailable in the database, enter another city or district nearby')
    else:
        break
# access weather data


w = Weather1(city_code1)        #use of Weather1 class
weather = w.Forecast()         #get the weather data using the city_code through openweather api
print(weather)
for key in weather:
    print(key,' = ', weather[key])
print('Temperature in  celsius: ',weather['main']['temp'] - 273.15)

crop = 'wheat'
f = ncbi(crop)
file = f.getncbi()
print(file)