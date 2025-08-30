import requests
from colorama import Fore, Style, init

init(autoreset=True) # Colorama init

API_KEY = "5903708844704c3caae194703253008"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    paramas = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }
    try:
        response = requests.get(BASE_URL, params=paramas, timeout=5)
        response.raise_for_status() # Handler for bd rp
        data = response.json()

        return {
            "city": data["location"]["name"],
            "region": data["location"]["region"],
            "country": data["location"]["country"],
            "temp": data["current"]["temp_c"], 
            "humidity": data["current"]["humidity"],
            "condition": data["current"]["condition"]["text"],
        }
    
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.RequestException:
        print(Fore.RED + "Network error ! Please check your internet connection.")
        return None

def main():
    print(Fore.CYAN + "=====***** Weather CLI App *****=====\n" + Style.RESET_ALL)
    city = input(Fore.YELLOW + "Enter Bitch's city name: " + Style.RESET_ALL)
    weather = get_weather(city)

    if weather:
        print(Fore.GREEN + f"\n🌍 City: {weather['city']}, {weather['region']}, {weather['country']}")
        print(Fore.RED + f"🌡️ Temperature: {weather['temp']}°C")
        print(Fore.BLUE + f"💧 Humidity: {weather['humidity']}%")
        print(Fore.MAGENTA + f"☁️ Condition: {weather['condition']}\n")
    else:
        print(Fore.RED + "Could not fetch weather. PLease check city name.")


if __name__ == "__main__":
    main()