from django.shortcuts import render
import json
import urllib
# Create your views here.

def index (request):
    # import ipdb;ipdb.set_trace
    if(request.method == 'POST'):
        city = request.POST['city']
        url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=fa3a3c55fa2dc5f3f97796bce61d1158'
        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)
        data={
            "country_code" : str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon']) + ' '+str(json_data['coord']['lat']),
            "temp" : str(json_data['main']['temp'])+'k',
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity'])
        }
    else : 
        city = ''
        data = {}
    return render(request, 'index.html', {'city' : city, 'data' : data})
