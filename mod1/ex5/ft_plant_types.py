class MyPlant():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


class Flower(MyPlant):
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self.color = color

    def bloom(self):
        print(f'{self.name} is blooming beautifully!')


class Tree(MyPlant):
    def __init__(self, name, age, height, diameter):
        super().__init__(name, age, height)
        self.trunk_diameter = diameter

    def produce_shade(self) -> None:
        print(f"{self.name} produced {self.height * 6} ",
              "square meters of shade")


class Vegetable(MyPlant):
    def __init__(self, name, age, height,  harvest_season, nutritional_value):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


oak = Tree("Oak", 500, 1800, 50)
rose = Flower("Rose", 20, 30, "red")
tomato = Vegetable("Tomato", 30, 50, "summer", "vitamin C")
palm = Tree("Palm", 700, 300, 40)
some_flower = Flower("My Flower", 20, 30, "blue")
cucumber = Vegetable("Cucumber", 20, 45, "summer", "fiber")

if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    print(f"{rose.name} (Flower), {rose.height}cm, {rose.color} color")
    rose.bloom()
    print(f"\n{oak.name} (Tree): {oak.height}cm, {oak.age} days",
          f"{oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print(f"\n{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days",
          f"{tomato.harvest_season} harvest",
          f"\n{tomato.name} is rich in {tomato.nutritional_value}!")
