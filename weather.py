import requests


class WeatherAPIError(Exception):
    pass


def get_current_weather(city: str, api_key: str, units: str = "metric") -> dict:
    if not city:
        raise WeatherAPIError("City name is required")
    if not api_key:
        raise WeatherAPIError("API key is required")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": units}

    resp = requests.get(url, params=params, timeout=10)
    if resp.status_code != 200:
        try:
            err = resp.json()
            message = err.get("message", resp.text)
        except Exception:
            message = resp.text
        raise WeatherAPIError(f"API request failed ({resp.status_code}): {message}")

    return resp.json()
