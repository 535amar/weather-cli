import requests
from colorama import Fore, Style, init
from tabulate import tabulate
from datetime import datetime

init(autoreset=True) # Colorama init

API_KEY = "5903708844704c3caae194703253008"
BASE_URL = "http://api.weatherapi.com/v1/forecast.json"

def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city,
        "days": 3,
        "aqi": "no",
        "alerts": "no"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        # Handle errors
        if "error" in data:
            print(Fore.RED + f"Error: {data['error']['message']}")
            return

        location = data['location']['name']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        emoji = get_weather_emoji(condition)

        print(Fore.CYAN + f"\n🌤️ Weather for {location}:")
        print(Fore.YELLOW + f"Temperature: {temp_c}°C")
        print(Fore.GREEN + f"Condition: {condition} {emoji}")
        print(Fore.BLUE + f"Humidity: {data['current']['humidity']}%")
        print(Fore.MAGENTA +  f"Wind: {data['current']['wind_kph']} km/h\n")

        # Forecast
        forecast_data = []
        for day in data['forecast']['forecastday']:
            date = datetime.strptime(day['date'], "%Y-%m-%d").strftime("%d-%b-%y")
            temp = day['day']['avgtemp_c']
            status = day['day']['condition']['text']
            status_emoji = get_weather_emoji(status)
            forecast_data.append([date, f"{temp}°C", f"{status_emoji} {status}"])
        
        print(Fore.CYAN + "3-Day Forecast:")
        print(Fore.GREEN + tabulate(forecast_data, headers=["Date", "Temp", "Status"], tablefmt="fancy_grid"))
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Network error:", e)

def get_weather_emoji(condition):
    condition = condition.lower()
    if "sun" in  condition or "clear" in condition:
        return "☀️"
    elif "cloud" in condition:
        return "☁️"
    elif "rain" in condition or "drizzle" in condition:
        return "🌧️"
    elif "thunder" in  condition:
        return "⛈️"
    elif "snow" in condition:
        return "❄️"
    elif "fog" in condition or "mist" in condition:
        return "🌫️"
    else:
        return "🌡️"
    
if __name__ == "__main__":
    print(Fore.CYAN + "======****** WEATHER CLI ******======\n" + Style.RESET_ALL)
    city = input(Fore.YELLOW + "Enter city name: " + Style.RESET_ALL)
    get_weather(city)