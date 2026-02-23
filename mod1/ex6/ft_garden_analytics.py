class Plant():
    """
    This is the base class for our plants
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Method to initialize the Plant

        :param name: name of our Plant
        :type name: str
        :param height: height of our Plant
        :type height: int
        :param age: age in days of our Plant
        :type age: int
        """
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0
        self.score_multiplier = 1

    def grow(self, size: int) -> None:
        """
        This is the method to grow our plant
        :param size: Description
        :type size: int
        """
        self.growth += size
        print(f"{self.name} grew {size}cm")

    def get_height(self) -> int:
        """
        This method returns us the height of our plant
        :return: The current height our plant
        :rtype: int
        """
        return self.height + self.growth

    def get_score(self) -> int:
        """
        This method returns us the score of the current plant
        :return: score points
        :rtype: int
        """
        return (self.height + self.growth) * self.score_multiplier


class FloweringPlant(Plant):
    def __init__(self, name, height, age, flower_color) -> None:
        super().__init__(name, height, age)
        self.flower_color = flower_color

    def set_color(self, flower_color) -> None:
        self.flower_color = flower_color

    def blooming(self) -> str:
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
        return cls(name)

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
    def height_validation(height: int) -> bool:
        """
        This is the method that helps us to understand if the height is valid
        """
        if height >= 0:
            return True
        else:
            return False

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
                    print(f"- {plant.name}: {plant.height}cm, "
                          f"{plant.flower_color} flowers "
                          f"{plant.blooming()}, "
                          f"Prize points: {plant.score_multiplier}")
                elif isinstance(plant, FloweringPlant):
                    flowering_plants += 1
                    print(f"- {plant.name}: {plant.height}cm, "
                          f"{plant.flower_color} flowers "
                          f"{plant.blooming()}")
                elif isinstance(plant, Plant):
                    regular_plants += 1
                    print(f"- {plant.name}: {plant.height}cm")
                total += 1
            print(
                f"\nPlants added: {total}, "
                f"Total growth: {gardener.growth * total}cm"
            )
            print(
                f"Plant types: {regular_plants} regular, "
                f" {flowering_plants} flowering,"
                f" {prize_flowers} prize flowers"
            )


def main() -> None:
    """
    This is the function to demonstrate
    the possibilities of GardenManager class
    """
    print("=== Garden Management System Demo ===\n")
    rose = FloweringPlant("Rose", 30, 50, "red")
    oak = Plant("Oak Tree", 1200, 1000)
    sunflower = PrizeFlower("Sunflower", 200, 100, "yellow")
    alice = Gardener("Alice")
    bob = Gardener("Bob")
    alice.add_plant(rose)
    alice.add_plant(oak)
    alice.add_plant(sunflower)
    alice.grow_help(1)
    bob.add_plant(sunflower)
    system = GardenManager.create_garden_network("Garden Managment System")
    system.add_gardners(alice)
    system.add_gardners(bob)
    system.GardenStats.report(alice)
    print(f"\nHeight validation test: {system.height_validation(9)}")
    system.scores()


if __name__ == "__main__":
    main()
