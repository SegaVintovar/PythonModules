class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)
    
class WaterError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)

def test() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    tomato = {"name": "tomato", "water": 0}
    try:
        if tomato["water"] < 1:
            raise PlantError(
                f"Caught PlantError: The {tomato["name"]} is wilting!"
            )
    except PlantError as e:
        print(str(e))
    print("\nTesting WaterError...")
    water_tank = 2
    try:
        if water_tank < 3:
            raise WaterError(
                "Caught WaterError: Not enough water in the tank!"
            )
    except WaterError as a:
        print(str(a))
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("Tomato is wilting")
    except GardenError as p:
        print(str(p))

    try:
        raise WaterError("Plants need more water")
    except GardenError as t:
        print(str(t))

test()