# --------------------
# Plant hierarchy
# --------------------

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_level):
        super().__init__(name, height, flower_color)
        self.prize_level = prize_level


# --------------------
# Garden Manager
# --------------------

class GardenManager:
    def __init__(self):
        self.gardens = {}

    # -------- instance methods --------
    def add_garden(self, garden_name):
        self.gardens[garden_name] = []

    def add_plant(self, garden_name, plant):
        if garden_name in self.gardens:
            self.gardens[garden_name].append(plant)

    def get_garden_stats(self, garden_name):
        plants = self.gardens.get(garden_name, [])
        return self.GardenStats.calculate(plants)

    # -------- class-level method --------
    @classmethod
    def create_garden_network(cls, garden_names):
        manager = cls()
        for name in garden_names:
            manager.add_garden(name)
        return manager

    # -------- utility method --------
    @staticmethod
    def is_prize_plant(plant):
        return isinstance(plant, PrizeFlower)

    # --------------------
    # Nested helper class
    # --------------------
    class GardenStats:
        @staticmethod
        def calculate(plants):
            total = len(plants)
            if total == 0:
                return {
                    "total_plants": 0,
                    "average_height": 0,
                    "prize_plants": 0
                }

            total_height = 0
            prize_count = 0

            for plant in plants:
                total_height += plant.height
                if isinstance(plant, PrizeFlower):
                    prize_count += 1

            return {
                "total_plants": total,
                "average_height": total_height / total,
                "prize_plants": prize_count
            }


manager = GardenManager.create_garden_network(["RoseGarden", "TulipGarden"])

manager.add_plant("RoseGarden", Plant("Fern", 30))
manager.add_plant("RoseGarden", FloweringPlant("Rose", 50, "Red"))
manager.add_plant("RoseGarden", PrizeFlower("Golden Rose", 60, "Gold", 1))

stats = manager.get_garden_stats("RoseGarden")
print(stats)
