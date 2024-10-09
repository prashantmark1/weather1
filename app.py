from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'a0e49925124713f52592ad2577925e70'  # Replace with your OpenWeatherMap API key

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form['city']
        data = get_weather(city)

        if data.get('cod') != 200:
            error_message = data.get('message', 'City not found!')
        else:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'pressure': data['main']['pressure'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description']
            }

    return render_template('index.html', weather_data=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
