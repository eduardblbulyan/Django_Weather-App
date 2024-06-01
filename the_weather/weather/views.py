from django.shortcuts import render
import requests

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=27f746592bf575aef976b1677b2f7e5d'
    city = 'Yerevan'
    r = requests.get(url.format(city)).json()
    city_data = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }
    context = {
        'city_data': city_data
    }

    return render(request, 'weather/weather.html',context=context)
