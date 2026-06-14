import os
import sys
from weather import get_current_weather


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <city> [units=metric|imperial]")
        sys.exit(1)

    city = sys.argv[1]
    units = sys.argv[2] if len(sys.argv) > 2 else "metric"

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Please set the OPENWEATHER_API_KEY environment variable.")
        sys.exit(2)

    try:
        data = get_current_weather(city, api_key=api_key, units=units)
    except Exception as e:
        print(f"Error fetching weather: {e}")
        sys.exit(3)

    name = data.get("name")
    weather = data.get("weather", [{}])[0]
    main_info = weather.get("main")
    description = weather.get("description")
    temp = data.get("main", {}).get("temp")

    print(f"Weather for {name}:")
    print(f"  {main_info} - {description}")
    print(f"  Temperature: {temp}° ({units})")


if __name__ == "__main__":
    main()
