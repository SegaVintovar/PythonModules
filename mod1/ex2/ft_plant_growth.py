class Plant:
    """
    This is a Plant class that serves as a blueprint for any plant
    """
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def get_info(self) -> None:
        """
        Method to print info about the plant
        """
        print(f'{self.name}: {self.height}cm, {self.days} days old')

    def age(self, to_add: int) -> None:
        """
        The method to add days to the age of our plant.
        Also it automatically adds +1 to the height.
        Our plants are growing +1cm per day.
        """
        self.days += to_add
        self.height += to_add
        self.get_info()

    def grow(self, to_add: int) -> None:
        """
        With this method we are adding height to our plant.
        This is useful if our plant grows faster then 1cm a day
        """
        self.height += to_add

def main() -> None:
    """This is a function to represent on how the Plant class works"""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant('Sunflower', 80, 45)
    cactus = Plant('Cactus', 15, 120)
    day1 = 1
    print(f'=== Day {day1} ===')
    rose.get_info()
    sunflower.get_info()
    cactus.get_info()
    day7 = 7
    print(f'=== Day {day7} ===')
    day_diff = day7 - day1
    rose.age(day_diff)
    sunflower.age(day_diff)
    cactus.age(day_diff)
    rose.get_info()
    sunflower.get_info()
    cactus.get_info()
    print(f'Growth this week +{day_diff}cm')


if __name__ == "__main__":
    main()
