import json

def average_by_city(log):
    totals = {}
    counts = {}
    for reading in log:
        city = reading["city"]
        if city in totals:
            totals[city] = totals[city] + reading["temp"]
            counts[city] = counts[city] + 1
        else:
            totals[city] = reading["temp"]
            counts[city] = 1
    averages = {}
    for city in totals:
        averages[city] = totals[city] / counts[city]
    return averages

with open(r"C:\Users\user\weather_log.json", "r") as file:
    log = json.load(file)
    
for city, average in average_by_city(log).items():
    print(f"{city}: average {average:.1f}")