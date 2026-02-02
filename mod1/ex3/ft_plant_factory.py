class MyPlant:
    '''This is a Plant class that serves as a blueprint for any plant.
      Also it informs us if the plant was creted and which parameters
        does it have'''
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
        print(f'Created: {self.name} ({self.height}cm, {self.days} days)')


if __name__ == "__main__":
    print('=== Plant Factory Output ===')
    plant1 = MyPlant('Weed', 50, 10)
    oat = MyPlant('Oat', 200, 365)
    rose = MyPlant("Rose", 25, 30)
    sunflower = MyPlant('Sunflower', 80, 45)
    cactus = MyPlant('Cactus', 15, 120)
    plant_list = [plant1, rose, sunflower, cactus, oat]
    i = 0
    for plant in plant_list:
        i += 1
    print(f'\nTotal plants created: {i}')
