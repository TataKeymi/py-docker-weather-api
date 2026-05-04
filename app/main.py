import os

import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"


def get_weather() -> None:
    if not API_KEY:
        raise Exception("API_KEY environment variable is not set")

    try:
        response = requests.get(URL)
        data = response.json()
        location = f"{data['location']['name']}/{data['location']['country']}"
        time = f"{data['location']['localtime']}"
        temperature = f"{data['current']['temp_c']}"
        condition = f"{data['current']['condition']['text']}"

        print(f"{location} {time} Weather: {temperature} Celsius, {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_weather()
