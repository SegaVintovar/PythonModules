class Plant:
    '''This is a Plant class that serves as a blueprint for any plant'''
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    """The program that manages data for 3 different plants"""
    print('=== Garden Plant Registry ===')
    rose = Plant('Rose', 25, 5)
    sunflower = Plant('Sunflower', 80, 45)
    cactus = Plant('Cactus', 15, 120)
    list = [rose, sunflower, cactus]
    i = 0
    while i < 3:
        print(f'{list[i].name}: {list[i].height}cm, {list[i].age} days old')
        i += 1

if __name__ == "__main__":
    main()