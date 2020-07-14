from pyowm import OWM

owm = OWM('ef2206ff5da67de63306d0b143e20872')  

# You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
#метод weather_at_place від імені інстансу owm 
#отримує інформацію в певному місті 
observation = owm.weather_at_place('Frankfurt')
#з змінної observation з допомогою 
#методу get_weather() отримуємо погоду
w = observation.get_weather()
# temperature=w.get_temperature('celsius')['temp']
# print(temperature)
# print("In Lviv city is now the temperature of the air"+
# " "+ str(temperature) + " for the Celsius")


print(w)                     # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
temperature=w.get_temperature('celsius')["temp"]
temperature_max=w.get_temperature('celsius')["temp_max"]# {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(f"Today temperature is {temperature}")

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#observation_list = owm.weather_around_coords(-22.57, -43.12)