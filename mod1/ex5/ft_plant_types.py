class Plant():
    """
    This is our base class for our plants
    """
    def __init__(self, name: str, age: int, height: int) -> None:
        """
        Initialization method for all plants

        :param name: Plant name
        :type name: str
        :param age: Plant age
        :type age: int
        :param height: Plant height
        :type height: int
        """
        self.name = name
        self.age = age
        self.height = height


class Flower(Plant):
    """
    Specialized class of our plant
    """
    def __init__(self, name: str, age: int, height: int, color: str) -> None:
        """
        Initialization method for all flowers

        :param color: Flower color
        :type color: str
        """
        super().__init__(name, age, height)
        self.color = color

    def bloom(self) -> None:
        """
        Flower method to let the flower bloom
        """
        print(f'{self.name} is blooming beautifully!')

    def print_info(self) -> None:
        """
        Method that prints info about flower
        """
        print(
            f"{self.name} (Flower): {self.height}cm, {self.age} days,"
            f" {self.color} color"
        )


class Tree(Plant):
    """
    Specialized class of our plant
    """
    def __init__(
            self, name: str, age: int, height: int, diameter: int
    ) -> None:
        """
        Initialization method for all trees

        :param diameter: diameter of the tree
        :type diameter: int
        """
        super().__init__(name, age, height)
        self.trunk = diameter

    def produce_shade(self) -> None:
        """
        This is the method to produce the shade
        """
        print(f"{self.name} produced {self.height * self.trunk} ",
              "square meters of shade")

    def print_info(self) -> None:
        """
        Method that prints info about tree
        """
        print(
            f"{self.name} (Tree): {self.height}cm, {self.age} days,"
            f" {self.trunk}cm diameter"
        )


class Vegetable(Plant):
    """
    Specialized class of our plant
    """
    def __init__(
            self, name: str, age: int, height: int,
            harvest_season: str, nutritional_value: str
    ) -> None:
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_info(self) -> None:
        """
        Method that prints info about vegie
        """
        print(
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days,"
            f" {self.harvest_season} harvest"
        )

    def nutritional_for(self) -> None:
        """
        This is the method to show nutritional value of the vegie
        """
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    """
    This is the function to represent
    how do we handle different types of plants
    """
    oak = Tree("Oak", 500, 1800, 50)
    rose = Flower("Rose", 20, 30, "red")
    tomato = Vegetable("Tomato", 30, 50, "summer", "vitamin C")
    palm = Tree("Palm", 700, 300, 40)
    some_flower = Flower("My Flower", 20, 30, "blue")
    cucumber = Vegetable("Cucumber", 20, 45, "summer", "fiber")
    my_plants = [oak, rose, tomato, palm, some_flower, cucumber]
    print("=== Garden Plant Types ===")
    for plant in my_plants:
        print()
        plant.print_info()
        if isinstance(plant, Flower):
            plant.bloom()
        if isinstance(plant, Tree):
            plant.produce_shade()
        if isinstance(plant, Vegetable):
            plant.nutritional_for()


if __name__ == "__main__":
    main()
