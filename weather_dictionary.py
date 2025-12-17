"""
Weather Dictionary Examples in Python

This module demonstrates various dictionary operations using weather-related data.
Dictionaries are key-value pairs that allow efficient data storage and retrieval.
"""


def demonstrate_dictionary_basics():
    """Demonstrate basic dictionary creation and operations."""
    print("=" * 60)
    print("1. CREATING DICTIONARIES")
    print("=" * 60)
    
    # Creating a simple weather dictionary
    weather = {
        "city": "New York",
        "temperature": 22.5,
        "condition": "Sunny",
        "humidity": 65,
        "wind_speed": 15
    }
    print(f"Weather dictionary: {weather}")
    
    # Creating an empty dictionary
    empty_weather = {}
    print(f"Empty dictionary: {empty_weather}")
    
    # Using dict() constructor
    weather_alt = dict(city="London", temperature=18.0, condition="Cloudy")
    print(f"Dictionary using dict(): {weather_alt}")
    print()


def demonstrate_accessing_values():
    """Demonstrate different ways to access dictionary values."""
    print("=" * 60)
    print("2. ACCESSING DICTIONARY VALUES")
    print("=" * 60)
    
    weather = {
        "city": "Paris",
        "temperature": 20.0,
        "condition": "Rainy",
        "humidity": 80
    }
    
    # Accessing using square brackets
    print(f"City: {weather['city']}")
    print(f"Temperature: {weather['temperature']}°C")
    
    # Using get() method (safer - returns None if key doesn't exist)
    print(f"Condition: {weather.get('condition')}")
    print(f"Wind speed: {weather.get('wind_speed', 'Not available')}")  # Default value
    print()


def demonstrate_modifying_dictionaries():
    """Demonstrate how to modify dictionary data."""
    print("=" * 60)
    print("3. MODIFYING DICTIONARIES")
    print("=" * 60)
    
    weather = {
        "city": "Tokyo",
        "temperature": 25.0,
        "condition": "Sunny"
    }
    print(f"Original: {weather}")
    
    # Adding new key-value pairs
    weather["humidity"] = 70
    weather["wind_speed"] = 12
    print(f"After adding keys: {weather}")
    
    # Modifying existing values
    weather["temperature"] = 26.5
    weather["condition"] = "Partly Cloudy"
    print(f"After modification: {weather}")
    
    # Removing items
    removed_value = weather.pop("wind_speed")
    print(f"Removed wind_speed: {removed_value}")
    print(f"After removal: {weather}")
    print()


def demonstrate_dictionary_methods():
    """Demonstrate useful dictionary methods."""
    print("=" * 60)
    print("4. DICTIONARY METHODS")
    print("=" * 60)
    
    weather = {
        "city": "Berlin",
        "temperature": 15.0,
        "condition": "Cloudy",
        "humidity": 75,
        "pressure": 1013
    }
    
    # keys() - Get all keys
    print(f"Keys: {list(weather.keys())}")
    
    # values() - Get all values
    print(f"Values: {list(weather.values())}")
    
    # items() - Get all key-value pairs
    print("Items:")
    for key, value in weather.items():
        print(f"  {key}: {value}")
    
    # update() - Merge dictionaries
    additional_data = {"wind_speed": 20, "visibility": 10}
    weather.update(additional_data)
    print(f"After update: {weather}")
    
    # clear() - Remove all items
    temp_dict = {"test": "value"}
    temp_dict.clear()
    print(f"Cleared dictionary: {temp_dict}")
    print()


def demonstrate_nested_dictionaries():
    """Demonstrate nested dictionaries for complex data structures."""
    print("=" * 60)
    print("5. NESTED DICTIONARIES")
    print("=" * 60)
    
    # Multi-city weather data
    weather_data = {
        "New York": {
            "temperature": 22,
            "condition": "Sunny",
            "humidity": 60,
            "forecast": {
                "tomorrow": "Partly Cloudy",
                "day_after": "Rainy"
            }
        },
        "London": {
            "temperature": 18,
            "condition": "Rainy",
            "humidity": 85,
            "forecast": {
                "tomorrow": "Cloudy",
                "day_after": "Sunny"
            }
        },
        "Tokyo": {
            "temperature": 25,
            "condition": "Clear",
            "humidity": 70,
            "forecast": {
                "tomorrow": "Clear",
                "day_after": "Partly Cloudy"
            }
        }
    }
    
    print("Multi-city weather data:")
    for city, data in weather_data.items():
        print(f"\n{city}:")
        print(f"  Temperature: {data['temperature']}°C")
        print(f"  Condition: {data['condition']}")
        print(f"  Tomorrow's forecast: {data['forecast']['tomorrow']}")
    print()


def demonstrate_dictionary_comprehension():
    """Demonstrate dictionary comprehension for creating dictionaries."""
    print("=" * 60)
    print("6. DICTIONARY COMPREHENSION")
    print("=" * 60)
    
    # Convert temperatures from Celsius to Fahrenheit
    temps_celsius = {
        "New York": 22,
        "London": 18,
        "Tokyo": 25,
        "Paris": 20,
        "Sydney": 28
    }
    
    temps_fahrenheit = {
        city: (temp * 9/5) + 32 
        for city, temp in temps_celsius.items()
    }
    
    print("Celsius temperatures:")
    for city, temp in temps_celsius.items():
        print(f"  {city}: {temp}°C")
    
    print("\nFahrenheit temperatures:")
    for city, temp in temps_fahrenheit.items():
        print(f"  {city}: {temp:.1f}°F")
    
    # Filter dictionary based on condition
    warm_cities = {
        city: temp 
        for city, temp in temps_celsius.items() 
        if temp > 20
    }
    print(f"\nCities warmer than 20°C: {warm_cities}")
    print()


def demonstrate_checking_keys():
    """Demonstrate checking for key existence."""
    print("=" * 60)
    print("7. CHECKING KEY EXISTENCE")
    print("=" * 60)
    
    weather = {
        "city": "Moscow",
        "temperature": 10,
        "condition": "Snow"
    }
    
    # Using 'in' keyword
    if "temperature" in weather:
        print(f"Temperature is available: {weather['temperature']}°C")
    
    if "wind_speed" not in weather:
        print("Wind speed data is not available")
    
    # Safe access with get()
    humidity = weather.get("humidity")
    if humidity is None:
        print("Humidity data is missing")
    else:
        print(f"Humidity: {humidity}%")
    print()


def demonstrate_default_dict():
    """Demonstrate using default values with dictionaries."""
    print("=" * 60)
    print("8. DEFAULT VALUES")
    print("=" * 60)
    
    # Using setdefault()
    weather = {"city": "Mumbai", "temperature": 32}
    
    # Set default value if key doesn't exist
    humidity = weather.setdefault("humidity", 85)
    print(f"Humidity: {humidity}")
    print(f"Updated weather: {weather}")
    
    # If key exists, setdefault returns existing value
    temp = weather.setdefault("temperature", 30)
    print(f"Temperature (unchanged): {temp}")
    print()


def demonstrate_practical_example():
    """Demonstrate a practical weather data management example."""
    print("=" * 60)
    print("9. PRACTICAL EXAMPLE: WEATHER DATA MANAGER")
    print("=" * 60)
    
    # Weather station data
    weather_stations = {}
    
    # Adding weather data for different stations
    def add_weather_reading(station_id, city, temp, condition):
        weather_stations[station_id] = {
            "city": city,
            "temperature": temp,
            "condition": condition,
            "timestamp": "2025-12-17 10:30:00"
        }
    
    # Add data
    add_weather_reading("WS001", "Chicago", 15, "Windy")
    add_weather_reading("WS002", "Miami", 30, "Sunny")
    add_weather_reading("WS003", "Seattle", 12, "Rainy")
    
    print("Weather Station Readings:")
    for station_id, data in weather_stations.items():
        print(f"\nStation {station_id}:")
        for key, value in data.items():
            print(f"  {key}: {value}")
    
    # Calculate average temperature
    avg_temp = sum(data["temperature"] for data in weather_stations.values()) / len(weather_stations)
    print(f"\nAverage temperature across all stations: {avg_temp:.1f}°C")
    print()


def demonstrate_copying_dictionaries():
    """Demonstrate shallow vs deep copying of dictionaries."""
    print("=" * 60)
    print("10. COPYING DICTIONARIES")
    print("=" * 60)
    
    # Original dictionary
    original = {
        "city": "Rome",
        "temperature": 24,
        "forecast": {"tomorrow": "Sunny"}
    }
    
    # Shallow copy using copy()
    shallow = original.copy()
    shallow["temperature"] = 25  # This won't affect original
    shallow["forecast"]["tomorrow"] = "Rainy"  # This WILL affect original (nested object)
    
    print(f"Original: {original}")
    print(f"Shallow copy: {shallow}")
    
    # Deep copy (requires import copy)
    import copy
    original2 = {
        "city": "Athens",
        "temperature": 28,
        "forecast": {"tomorrow": "Hot"}
    }
    deep = copy.deepcopy(original2)
    deep["forecast"]["tomorrow"] = "Very Hot"  # Won't affect original2
    
    print(f"\nOriginal2: {original2}")
    print(f"Deep copy: {deep}")
    print()


def main():
    """Main function to run all demonstrations."""
    print("\n" + "=" * 60)
    print("PYTHON DICTIONARY DEMONSTRATIONS FOR WEATHER APP")
    print("=" * 60 + "\n")
    
    demonstrate_dictionary_basics()
    demonstrate_accessing_values()
    demonstrate_modifying_dictionaries()
    demonstrate_dictionary_methods()
    demonstrate_nested_dictionaries()
    demonstrate_dictionary_comprehension()
    demonstrate_checking_keys()
    demonstrate_default_dict()
    demonstrate_practical_example()
    demonstrate_copying_dictionaries()
    
    print("=" * 60)
    print("ALL DEMONSTRATIONS COMPLETED!")
    print("=" * 60)


if __name__ == "__main__":
    main()
