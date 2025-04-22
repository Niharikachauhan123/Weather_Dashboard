import requests
from datetime import datetime

WEATHERAPI_KEY = "d11086cbdc19454fb40123138251904"
WEATHERAPI_URL = "http://api.weatherapi.com/v1/forecast.json"

def get_weatherapi_forecast(query):
    url = f"{WEATHERAPI_URL}?key={WEATHERAPI_KEY}&q={query}&days=7&aqi=no&alerts=yes"
    return requests.get(url).json()

def get_coordinates_from_place(place_name):
    try:
        if len(place_name.split()) == 1:
            place_name += ", Himachal Pradesh"
        response = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": place_name, "format": "json"},
            headers={"User-Agent": "weather-app-streamlit"}
        )
        results = response.json()
        if results:
            return results[0]["lat"], results[0]["lon"]
        else:
            return None, None
    except Exception:
        return None, None

def condition_to_emoji(cond):
    cond = cond.lower()
    if "sun" in cond or "clear" in cond:
        return "☀️"
    elif "cloud" in cond:
        return "☁️"
    elif "rain" in cond:
        return "🌧️"
    elif "thunder" in cond:
        return "⛈️"
    elif "snow" in cond:
        return "❄️"
    elif "fog" in cond or "mist" in cond:
        return "🌫️"
    else:
        return "🌈"
