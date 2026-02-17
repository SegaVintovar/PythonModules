def check_plant_health(plant_name, water_level, sunlight_hours):
    if len(plant_name) < 1:
        raise ValueError(
            "Error: Plant name cannot be empty!"
        )
    if water_level < 1:
        raise ValueError(
            f"Error: Water level {water_level}"
            " is too low (min 1)"
        )
    if water_level > 10:
        raise ValueError(
            f"Error: Water level {water_level} is too high (max 10)"
        )
    if sunlight_hours < 2:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
        )
    if sunlight_hours > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    else:
        print(f"Plant '{plant_name}' is healthy!")

def  test_plant_checks():
    try:
        print("Testing good values...")
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(str(e))
    try:
        print("Testing empty plant name...")
        check_plant_health("", 5, 5)
    except ValueError as p:
        print(str(p))
    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 20, 5)
    except ValueError as t:
        print(str(t))
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, 128)
    except ValueError as c:
        print(str(c))
    print("All error raising tests completed!")

test_plant_checks()