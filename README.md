# Weather API Integration

Simple Python CLI to fetch current weather using OpenWeatherMap.

Requirements
- Python 3.8+
- `requests` library

Setup
1. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Set your OpenWeatherMap API key as an environment variable:

Windows (PowerShell):

```powershell
$env:OPENWEATHER_API_KEY = "your_api_key_here"
```

Unix/macOS:

```bash
export OPENWEATHER_API_KEY=your_api_key_here
```

Usage

```bash
python main.py "London" metric
```

Examples

- `python main.py "New York" imperial`
- `python main.py Tokyo`

Files
- `main.py`: CLI entrypoint
- `weather.py`: API integration logic

Notes
- This project uses the OpenWeatherMap current weather endpoint. Replace or extend with other endpoints as needed.
