class SecurePlant:
    """
    This the class that shows us on how we can securely add height and age
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, size: int) -> None:
        """
        This is the method to set the height of the plant.
        If height is < 0 we do not let the user perform height adjustment
        """
        if size >= 0:
            self.__height = size
        else:
            print(f'Invalid operation attempted: height {size}cm [REJECTED]')
            print('Security: Negative height rejected')

    def set_age(self, age: int):
        """
        This is the method to set the age of the plant.
        If hte age is < 0 we do not let the user perform height adjustment
        """
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
