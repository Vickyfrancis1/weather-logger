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
        
def test_average_two_readings():
    log = [
        {"city": "Lagos", "temp": 28.0, "time": "t1"},
        {"city": "Lagos", "temp": 30.0, "time": "t2"},
    ]
    assert average_by_city(log) == {"Lagos": 29.0}
      
def test_empty_log():
    assert average_by_city([]) == {}
    
def test_two_cities():
    log = [
        {"city": "Lagos", "temp": 30.0, "time": "t1"},
        {"city": "Abuja", "temp": 26.0, "time": "t2"},
    ]
    assert average_by_city(log) == {"Lagos": 30.0, "Abuja": 26.0}
        