import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "db46dbf2104c4a22d6a7ae54125576e3"
city = "Jamshedpur"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print("API Response:", data)

weather = {
    'Temperature (°C)': data['main']['temp'],
    'Feels Like (°C)': data['main']['feels_like'],
    'Humidity (%)': data['main']['humidity'],
    'Pressure (hPa)': data['main']['pressure'],
    'Wind Speed (m/s)': data['wind']['speed']
}

print("Weather Data:", weather)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
plt.title(f"Weather in {city}", fontsize=16)

keys = list(weather.keys())
values = list(weather.values())

sns.barplot(x=keys, y=values)
plt.xticks(rotation=30)
plt.ylabel("Values")
plt.tight_layout()
plt.show()
