# weather-logger

A Python tool that records live temperatures for Nigerian cities and reports the average per city.

## Features

- Fetches live weather from the free Open-Meteo API using `requests`
- Skips cities that fail, so one error never stops the run
- Saves every reading with a timestamp to a JSON log
- Report of the average temperature per city
- Unit tests with pytest
- Can run daily with Windows Task Scheduler

## Setup

```
pip install requests pytest
```

## How to run

Change the log file path in both scripts (`C:\Users\user\weather_log.json`) to a folder on your own computer, then run:

```
python weather_log.py
python weather_report.py
```

## Run the tests

```
python -m pytest test_weather_report.py
```

## Run it automatically (Windows)

1. Open Task Scheduler and choose Create Basic Task.
2. Trigger: Daily.
3. Action: Start a program.
4. Program: the path to your `python.exe`.
5. Arguments: the full path to `weather_log.py`.

## Author

Victor Amuta
