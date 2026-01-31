class MyPlant:
    '''This is a Plant class that serves as a blueprint for any plant'''
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
    # def grow(self):
    #     self.height += 1

    def get_info(self):
        print(f'{self.name}: {self.height}cm, {self.days} days old')

    def age(self, to_add):
        self.days += to_add
        self.height += to_add
        get_info(self)

    def grow(self, to_add):
        self.height += to_add

    def get_info(self):
        print(f'{self.name}: {self.height}cm, {self.days} days old')


if __name__ == "__main__":
    rose = MyPlant("Rose", 25, 30)
    sunflower = MyPlant('Sunflower', 80, 45)
    cactus = MyPlant('Cactus', 15, 120)
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
