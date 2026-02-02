class MyPlant():
	def __init__(self, name, age, height):
		self.name = name
		self.age = age
		self.height = height

class Flower(MyPlant):
	def __init__(self, name, age, height, color):
		MyPlant.__init__(name, age, height)
		self.color = color
	def blooming(self):
		print(f'{self.name} is blooming beautifully!')
	
	# super().__init__(name, age, height)
class Tree(MyPlant):
	def __init__(self, name, age, height, diameter):
		super().__init__(name, age, height)
		self.trunk_diameter = diameter

	def produce_shade(self) -> None:
		print(f"{self.name} produced {self.height * 6} "
		"square meters of shade")

class Vegatable(MyPlant):
	def __init__(self, name, age, height,  harvest_season, nutritional_value):
		super().__init__(name, age, height)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value
	
oak = Tree("Oak", 500, 1800, 50)
oak.produce_shade()
print()