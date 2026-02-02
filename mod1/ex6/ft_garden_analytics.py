class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, size):
        self.height += size
        print(f"{self.name} grew {size}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
        
    def set_color(self, flower_color):
        self.flower_color = flower_color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, flower_color, is_prize):
        super().__init__(name, height, age)
        if (flower_color == "red"):
            self.is_prize = True
        else:
            self.is_prize = False

    # Instance method
    def is_it_a_prize(self):
        if self.is_prize:
            print("This Flowering Plant is a prize")
        else:
            print("This Plant is not a prize")


class GardenManager():
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def growth(self, height):
        for plant in self.plants:
            plant.grow(height)

    @classmethod
    def create_garden_network(cls):
        ...

    @staticmethod
    def static_example():
        ...

    class GardenStats():
        """
        Nested statistics helper to calculate analytics
        """
        def report():
            ...


rose = FloweringPlant("Rose", 30, 50)
alice = GardenManager("Alice")
alice.add_plant(rose)
alice.growth(3)
