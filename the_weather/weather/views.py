from django.shortcuts import render
import requests
from .models import City

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=27f746592bf575aef976b1677b2f7e5d'
    # city = 'Yerevan'

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    print(weather_data)
    context = {
        'weather_data': weather_data
    }
    return render(request, 'weather/weather.html', context=context)
