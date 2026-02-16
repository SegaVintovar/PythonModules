class WateringError(Exception):
    def __init__(self, plant):
        self.plant = plant
        super().__init__(f"Error: Cannont water {self.plant} - invalid plant!")

def water_plants(plant_list):
    our_plants = ["tomato", "lettuce", "carrots"]
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant in our_plants:
                print(f"Watering {plant}")
            else:
                raise WateringError(plant)
    except WateringError as a:
        print(str(a))
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    print("== Garden Watering System ===", "\n\nTesting normal watering...")
    water_plants(plant_list=["tomato", "lettuce", "carrots"])
    print("\nTesting with error...")
    water_plants(plant_list=[None])

    print("\nCleanup always happens, even with errors!")

test_watering_system()