class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)

class Plant():
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    def add_water(self, water: int) -> None:
        self.water_level += water


class GardenManager():
    def __init__(self, water_tank: int):
        self.plants: list = []
        self.water_tank = water_tank

    def add_plant(self, plant: Plant) -> None:
        # try:
            if len(plant.name) > 0:
                self.plants.append(plant)
                print(f"Added {plant.name} successfully")
            else:
                raise PlantError(
                    "Error adding plant: Plant name cannot be empty!"
                )
        # except PlantError as e:
        #     print(str(e))
    
    def watering_plants(self, water: int) -> None:
        print("Opening watering system")
        # try:
        for plant in self.plants:
            self.water_tank -= water
            if self.water_tank < 1:
                raise GardenError(
                    "Caught GardenError: Not enough water in tank"
                )
            else:
                plant.add_water(water)
                print(f"Watering {plant.name} - success")
        # 

    def check_plant_health(self) -> None:
        try:
            for plant in self.plants:
                if plant.water_level < 1:
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        f"Water level {plant.water_level}"
                        " is too low (min 1)"
                    )
                if plant.water_level > 10:
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        f"Water level {plant.water_level} "
                        "is too high (max 10)"
                    )
                if plant.sunlight_hours < 2:
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        f"Sunlight hours {plant.sunlight_hours} "
                        "is too low (min 2)"
                    )
                if plant.sunlight_hours > 12:
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        f"Sunlight hours {plant.sunlight_hours}",
                        " is too high (max 12)"
                    )
                else:
                    print(
                        f"{plant.name}: healthy (water: {plant.water_level},"
                        f" sun: {plant.sunlight_hours})"
                    )
        except ValueError as e:
            print(str(e))

    def garden_check(self):
        try:
            if self.water_tank < len(self.plants):
                raise GardenError(
                    "Caught GardenError: Not enough water in tank"
                )
        except GardenError as e:
            print(str(e))
        else:
            print("Garden has enough water in the tank: "
                  f"{self.water_tank} liters")
        finally:
            print("System recovered and continuing...")


def test_garden_management():
    print("=== Garden Management System ===")
    garden = GardenManager(9)
    tomato = Plant("tomato", 5, 8)
    lettuce = Plant("lettuce", 9, 9)
    error = Plant("", 12, 13)
    print("\nAdding plants to garden...")
    try:
        garden.add_plant(tomato)
        garden.add_plant(lettuce)
        garden.add_plant(error)
    except PlantError as e:
        print(str(e))
    print("\nWatering plants...")
    try:
        garden.watering_plants(3)
    except GardenError as e:
        print(str(e))
    finally:
        print("Closing watering system (cleanup)")
    print("\nChecking plant health...")
    garden.check_plant_health()
    print("\nTesting error recovery...")
    garden.garden_check()
    print("\nGarden management system test complete!")


test_garden_management()