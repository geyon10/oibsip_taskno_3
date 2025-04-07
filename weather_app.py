import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print(f"❌ Error: {data['message']}")
            return

        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].capitalize()

        print(f"\n🌍 Weather in {city}, {country}:")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌥️ Condition: {condition}\n")

    except Exception as e:
        print("⚠️ Something went wrong:", e)

def main():
    print("=== 🌦️ Command-Line Weather App ===")
    api_key = input("Enter your OpenWeatherMap API Key: ")
    location = input("Enter a city name or ZIP code: ")

    get_weather(api_key, location)

if __name__ == "__main__":
    main()
