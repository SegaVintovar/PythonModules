class Plant:
    '''This is a Plant class that serves as a blueprint for any plant.
      Also it informs us if the plant was creted and which parameters
        does it have'''
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days
        print(f'Created: {self.name} ({self.height}cm, {self.days} days)')

def factory() -> None:
    """
    The function to represent how initialize the class member
    with dunder(__) method.
    """
    print('=== Plant Factory Output ===')
    plant1 = Plant('Weed', 50, 10)
    oat = Plant('Oat', 200, 365)
    rose = Plant("Rose", 25, 30)
    sunflower = Plant('Sunflower', 80, 45)
    cactus = Plant('Cactus', 15, 120)
    plant_list = [plant1, rose, sunflower, cactus, oat]
    i = 0
    for _ in plant_list:
        i += 1
    print(f'\nTotal plants created: {i}')

if __name__ == "__main__":
    factory()