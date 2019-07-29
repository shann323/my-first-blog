from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import time



# Create your views here.

#search page
def search(request):
    return render(request, 'index.html')




#forecast page
def forecast(request):
    
    c = request.POST['city']
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=7fee53226a6fbc936e0308a3f4941aaa&units=metric'.format(c)
    r = requests.get(url)
    if r.status_code == 404:
            messages.info(request, 'Error: You have entered wrong city name!')
            return redirect('/')
    else:
            data = r.json()
            localtime = time.asctime( time.localtime(time.time()) )
            weather = {
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'city': c.title(),
                'temperature': data['main']['temp'],
                'localtime': localtime
                 }
            print(r)
            return render(request, 'weather.html', {'weather': weather})

    
