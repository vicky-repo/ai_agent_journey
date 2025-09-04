import requests
def get_weather_data (city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    full_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    print(f"Fetching weather data for: {city}")
    response = requests.get(full_url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        current_temperature = data['main']['temp']
        return f"The weather in {city} is {weather_description} with a temperature of {current_temperature}°C."
    else:
        return f"Error: Could not retrieve weather data: Status code {response.status_code}"
    
My_API_KEY = "fb72866f2d6f4d878e35877b5ae44971"
city1 = "Bihar"
city2 = "Halua"

weather_report = get_weather_data(city1, My_API_KEY)
print(weather_report)
weather_report1 = get_weather_data(city2, My_API_KEY)
print(weather_report1)


