import json
import requests
from datetime import datetime

def load_log(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_log(filename, log):
    with open(filename, "w") as file:
        json.dump(log, file, indent=2)

def get_temperature(latitude, longitude):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}&current_weather=true"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()["current_weather"]["temperature"]
    except requests.exceptions.RequestException:
        return None
    
def make_reading(city, temp):
    return {
        "city": city,
        "temp": temp,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
     }

cities = [
    ("Lagos", 6.52, 3.38),
    ("Abuja", 9.08, 7.40),
    ("Owerri", 5.48, 7.03),
    ("Port Harcourt", 4.82, 7.03),
 ]   

readings = []

for city, lat, lon in cities:
    temp = get_temperature(lat, lon)
    if temp is None:
        print(f"Could not get {city}.")
        continue
    readings.append(make_reading(city, temp))
    
for reading in readings:
    print(f"{reading['city']}: {reading['temp']}")

log = load_log(r"C:\Users\user\weather_log.json")
log.extend(readings)
save_log(r"C:\Users\user\weather_log.json", log)
print(f"Saved. The log now has {len(log)} readings.")