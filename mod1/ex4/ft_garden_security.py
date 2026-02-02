class SecurePlant:
	def __init__(self, name, height, age):
		self.name = name
		self.__height = height
		self.__age = age


	def set_height(self, size):
		if size >=0:
			self.__height = size
		else:
			print(f'Invalid operation attempted: height {size}cm [REJECTED]')
			print('Security: Negative height rejected')


	def set_age(self, age):
		if age >= 0:
			self.__age = age
		else:
			print(f'Invalid operation attempted: age {age}cm [REJECTED]')
			print('Security: Negative age rejected')


	def get_age(self):
		return self.__age


	def get_height(self):
		return self.__height

def main():
	rose = SecurePlant("Rose", 35, 45)
	print(rose.get_height())
	rose.set_height(3)


if __name__ == "__main__":
	main()