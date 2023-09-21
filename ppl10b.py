import json

# Load the JSON data from the file
with open('weather_data.json') as f:
    data = json.load(f)

# Extract the required weather data
city = data['main']['city']
current_temp = data['main']['temp']
humidity = data['main']['humidity']
weather_desc = data['weather'][0]['description']

# Display the weather data
print(f"City : {city}")
print(f"Current temperature: {current_temp}°C")
print(f"Humidity: {humidity}%")
print(f"Weather description: {weather_desc}")
