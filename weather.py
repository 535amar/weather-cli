import requests
from colorama import Fore, Style, init

init(autoreset=True) # Colorama initialized


API_KEY = "c356a2c0a93bd675f2fc06f06bfc8f1d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params ={
        "q": city,
        "appid": API_KEY,
        "units": "metric" # Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status() # For bad responses errors
        data = response.json()
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"]
        }
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.RequestException:
        print(Fore.RED + "Network error ! Please check your internet connection.")
        return None
    
def main():
    print(Fore.CYAN + "====***** Weather CLI App *****====\n" + Style.RESET_ALL)
    city = input(Fore.YELLOW + "Enter city name: " + Style.RESET_ALL)
    weather = get_weather(city)

    if weather:
        print(Fore.GREEN + f"\n🌍 City: {weather['city']}")
        print(Fore.RED + f"🌡️ Temperature: {weather[ 'temp']}°C")
        print(Fore.BLUE + f"💧 Humidity: {weather[ 'humidity']}%")
        print(Fore.MAGENTA + f"☁️ Condition: {weather['condition'].title()}\n")
    else:
        print(Fore.RED + "Could not fetch weather. Please check city name.")

if __name__ == "__main__":
    main()