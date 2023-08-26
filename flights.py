import json
import random
from datetime import datetime


def get_flights():
    cities = ["New York", "London", "Paris", "Tokyo",
              "Sydney", "Los Angeles", "Singapore", "Berlin"]
    plane_types = ["Boeing 747", "Airbus A320", "Boeing 777", "Airbus A380"]
    times = [datetime(2023, 9, 1, i, random.choice(range(60)))
             for i in range(24)]

    flight_data = []
    for _ in range(10):
        departure_city = random.choice(cities)
        destination_city = random.choice(
            list(filter(lambda x: x != departure_city, cities)))
        departure_time = random.choice(times)
        duration = random.randint(2, 15)
        airplane_type = random.choice(plane_types)
        price = random.uniform(100.0, 1500.0)

        flight_data.append({
            "departure_city": departure_city,
            "destination_city": destination_city,
            "departure_time": departure_time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration_hours": duration,
            "airplane_type": airplane_type,
            "price": round(price, 2)
        })

    return json.dumps(flight_data, indent=4)
