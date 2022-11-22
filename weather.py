import requests

API_KEY = "bd297fbd10bc072c4a6c09933039b4ba"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"], 2)
    fConversion = round(1.8 * (temperature - 273.15) + 32, 2)

    print ("Weather:", weather)
    print ("Temperature:", fConversion, "fahrenheit")


else:
    print("An error occurred.")

