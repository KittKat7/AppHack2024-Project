import requests


def get_user_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        city = data.get("city")
        if city:
            return city
        else:
            print("City information not found in the response.")
            return None
    except Exception as e:
        print("Error occurred while fetching user location:", str(e))
        return None


def queryWeather(city = None):
    if city is None:
        city=get_user_location()

    url = f"https://wttr.in/{city}?format=%t+%C+%w+%h"
    response = requests.get(url)

    if response.status_code == 200:
        return f"{city} is {response.text}"
    else:
        return("Failed to retrieve weather data. Status code:", response.status_code)



