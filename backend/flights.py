import json
import random
from datetime import datetime


def get_flights():

    data = {
        "flights": [
            {
                "flight_id": "AA123",
                "departure_time": "09:00",
                "destination_time": "12:00",
                "departure_city": "New York",
                "destination_city": "Los Angeles",
                "price": "$300",
                "seat_availability": {
                    "economy": 25,
                    "business": 5,
                    "first_class": 2
                },
                "flight_status": "On Time",
                "gate": "B12",
                "in_flight_services": {
                    "meals": ["vegan", "chicken", "beef"],
                    "wifi": True,
                    "entertainment": ["movies", "music", "games"]
                },
                "loyalty_points_earned": 500
            },
            {
                "flight_id": "AA456",
                "departure_time": "15:00",
                "destination_time": "18:30",
                "departure_city": "Chicago",
                "destination_city": "Miami",
                "price": "$220",
                "seat_availability": {
                    "economy": 50,
                    "business": 10,
                    "first_class": 0
                },
                "flight_status": "Delayed",
                "gate": "C7",
                "in_flight_services": {
                    "meals": ["vegan", "seafood"],
                    "wifi": False,
                    "entertainment": ["movies", "games"]
                },
                "loyalty_points_earned": 400
            }
        ],
        "airport_services": {
            "New York": {
                "lounges": ["Admirals Club", "Priority Pass"],
                "shops": ["Duty-Free", "TechStore"],
                "restaurants": ["Starbucks", "Burger King"]
            },
            "Los Angeles": {
                "lounges": ["Centurion Lounge", "Admirals Club"],
                "shops": ["Fashion Boutique", "Tech Haven"],
                "restaurants": ["Pizza Express", "Taco Bell"]
            }
        }
    }

    return json.dumps(data, indent=4)
