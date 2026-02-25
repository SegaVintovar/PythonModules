def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
        ) -> None:
    if plant_name == "":
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


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    try:
        print("\nTesting good values...")
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(str(e))
    try:
        print("\nTesting empty plant name...")
        check_plant_health("", 5, 5)
    except ValueError as p:
        print(str(p))
    try:
        print("\nTesting bad water level...")
        check_plant_health("tomato", 15, 5)
    except ValueError as t:
        print(str(t))
    try:
        print("\nTesting bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as c:
        print(str(c))
    finally:
        print("\nAll error raising tests completed!")
