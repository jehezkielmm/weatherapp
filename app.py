from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
import requests, os

app = Flask(__name__)
app.config['DEBUG']= True

@app.route('/', methods=['GET'])
def indexGet():
    return render_template('weather.html', currentweather='')

@app.route('/',  methods=['POST'])
def indexPost():
    city = request.form.get('city')
    url = 'https://us1.locationiq.com/v1/search.php?key=4c642a89171914&format=json&q=' + city
    loc = requests.get(url).json()
    lat = loc[0]['lat']
    lon = loc[0]['lon']

    darkSkyApiUrl = 'https://api.darksky.net/forecast/43e6dd34df45838adb3e57f8634457af/' + lat + ',' + lon
    weather = requests.get(darkSkyApiUrl).json()

    tempfahrenheit = weather['currently']['temperature']
    tempcelsius = str(((tempfahrenheit-32)*(5/9))) + ' C'

    currentweather = {
        'temperature': tempcelsius,
        'city': city,
        'description': weather['currently']['summary'],
    }
    return render_template('weather.html', currentweather = currentweather)

