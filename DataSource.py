import requests
s_city = "Petersburg,RU"
city_id = 472757
appid = '27aa0b5f5cef20217a56cc98bd112f2f'
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'type': 'like', 'units': 'metric', 'land' : 'ry' , 'APPID': appid})
    data = res.json()
    ret = (f"conditions:{data['weather'][0]['description']} \n"
           f"temp {data['main']['temp']} \n"
           f"temp_min {data['main']['temp_min']} \n"
           f"temp_max {data['main']['temp_max']} \n"
           f"wind {data['wind']['speed']} m/s \n"
           f"humidity {data['main']['humidity']} % \n"
           f"pressure {round(data['main']['pressure'] * 0.7501, 2)} mm Rtytnogo Stolba")
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
    print('wind:', data['wind']['speed'])
    print('humidity:', data['main']["humidity"])
    print('pressure:', round(data['main']['pressure'] * 0.7501, 2))
except Exception as e:
    print("Exception (weather):", e)
    pass