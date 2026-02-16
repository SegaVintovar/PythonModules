class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)
    
class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)

def test():
    try:
        raise PlantError("Tomato is wilting")
    except PlantError as e:
        print(str(e))

    try:
        raise WaterError("Plants need more water")
    except WaterError as a:
        print(str(a))

    try:
        raise PlantError("Tomato is wilting")
    except GardenError as p:
        print(str(p))

    try:
        raise WaterError("Plants need more water")
    except GardenError as t:
        print(str(t))