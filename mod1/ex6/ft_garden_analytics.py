class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0
        self.score_multiplier = 1

    def grow(self, size):
        self.growth += size
        print(f"{self.name} grew {size}cm")
    
    def get_height(self):
        return self.height + self.growth
    
    def get_score(self):
        return (self.height + self.growth) * self.score_multiplier


class FloweringPlant(Plant):
    def __init__(self, name, height, age, flower_color):
        super().__init__(name, height, age)
        self.flower_color = flower_color

    def set_color(self, flower_color):
        self.flower_color = flower_color

    def blooming(self):
        return "(blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, flower_color):
        super().__init__(name, height, age, flower_color)
        self.score_multiplier = 4


class Gardener():
    def __init__(self, name: str):
        self.name = name
        self.plants = []
        self.growth = 0

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_help(self, growth: int):
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(growth)
        self.growth += growth

    def get_growth(self):
        return self.growth

class GardenManager():
    def __init__(self, name: str):
        self.name = name
        self.gardeners = []

    def add_gardners(self, gardener: Gardener):
        self.gardeners.append(gardener)

    @classmethod
    def create_garden_network(cls, name: str):
        return  cls(name)

    def scores(self):
        print('Garden scores - ', end='')
        total_gardens = 0
        for gardener in self.gardeners:
            garden_score = 0
            for plant in gardener.plants:
                garden_score += plant.get_score()
            print(f"{gardener.name}: {garden_score}, ", end="")
            total_gardens += 1
        print(f"\nTotal gardens managed: {total_gardens}")

    @staticmethod
    def height_validation(self, gardeners):
        ...

    class GardenStats():
        """
        Nested statistics helper to calculate analytics
        """
        def __init__(self, gardners):
            self.gardners = gardners

        def report(gardener: Gardener):
            print(f"\n=== {gardener.name}'s Garden Report ===")
            print("Plants in garden:")
            total = 0
            regular_plants = 0
            flowering_plants = 0
            prize_flowers = 0
            for plant in (gardener.plants):
                if isinstance(plant, PrizeFlower):
                    prize_flowers += 1
                    print(f"{plant.name}: {plant.height}cm, " 
                          f"{plant.flower_color} flowers "
                          f"{plant.blooming()}, "
                          f"Prize points: {plant.score_multiplier}")
                elif isinstance(plant, FloweringPlant):
                    flowering_plants += 1
                    print(f"{plant.name}: {plant.height}cm, " 
                          f"{plant.flower_color} flowers "
                          f"{plant.blooming()}")
                elif isinstance(plant, Plant):
                    regular_plants += 1
                    print(f"{plant.name}: {plant.height}cm")
                total += 1
            print(f"Plants added: {total}, Total growth: {gardener.growth}")
            print(f"Plant types: {regular_plants} regular, "
                   f" {flowering_plants} flowering,"
                   f" {prize_flowers} prize flowers")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    rose = FloweringPlant("Rose", 30, 50, "red")
    oak = Plant("Oak Tree", 1200, 1000)
    sunflower = PrizeFlower("Sunflower", 200, 100, "yellow")
    alice = Gardener("Alice")
    bob = Gardener("Bob")
    alice.add_plant(rose)
    alice.add_plant(oak)
    alice.add_plant(sunflower)
    alice.grow_help(3)
    bob.add_plant(sunflower)
    system = GardenManager.create_garden_network("Garden Managment System")
    system.add_gardners(alice)
    system.add_gardners(bob)
    system.GardenStats.report(alice)
    system.scores()
# system.growth(3)
