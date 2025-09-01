# 🌤️ Weather CLI

A simple and interactive command-line application to fetch **real-time weather** and a **3-day forecast** for any city using the [WeatherAPI](https://www.weatherapi.com/).  

---

## ✨ Features
- 🌡️ Current temperature, condition, humidity, and wind speed  
- 📅 3-day weather forecast with condition summaries  
- ❌ Error handling for invalid city names or API issues  
- 🎨 Clean CLI output with emojis for better readability  

---

## 🚀 Getting Started

### 1. Clone the Repository
git clone https://github.com/535amar/weather-cli.git
cd weather-cli
### 2. Create & Activate Virtual Environment (Optional)
pyhthon3 -m venv venv
source venv/bin/activate # On Linux
venv\Scripts\activate    # On Windows

### 3. Install Dependencies
pip install -r requirements.txt
### 4. Add Your API Key
 . Sign up at WeatherAPI
 . Get your API Key
 . Replace the *API_Key* value in the script with your key
   
   API_KEY = "your_api_key_here

### 5. Run the Program
python3 weather_ltr.py

🛠️ Built With

.Python 3
.WeatherAPI
.Requests
.Colorama
