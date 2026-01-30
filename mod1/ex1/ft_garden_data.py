class MyPlant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
Rose = MyPlant('Rose', 25, 5)
print(Rose.name, Rose.age, Rose.height)
