class MyPlant:
    '''This is a Plant class that serves as a blueprint for any plant'''
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
    # def grow(self):
    #     self.height += 1

    def age(self, to_add):
        self.days += to_add
        self.height += to_add

    def grow(self, to_add):
        self.height += to_add

    def get_info(self):
        print(f'{self.name}: {self.height}cm, {self.days} days old')