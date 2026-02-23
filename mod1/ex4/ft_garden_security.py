class SecurePlant:
    """
    This the class that shows us on how we can securely add height and age
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def set_height(self, size: int) -> None:
        """
        This is the method to set the height of the plant.
        If height is < 0 we do not let the user perform height adjustment
        """
        if size >= 0:
            self.__height = size
            print(f"Height updated: {self.__height}cm [OK]")
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
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f'Invalid operation attempted: age {age}cm [REJECTED]')
            print('Security: Negative age rejected')

    def get_age(self):
        """
        This method returns us the age of the SecurePlant
        """
        return self.__age

    def get_height(self):
        """
        This method returns us the height of the SecurePlant
        """
        return self.__height

    def show_info(self) -> None:
        """
        This is the method to show the info if the current Plant
        """
        print(
            f"Current plant: {self.name} ({self.get_height()}cm,"
            f" {self.get_age()})"
        )


def main():
    """
    This is the function to represent how securely use SecurePlant
    """
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 35, 45)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    rose.show_info()


if __name__ == "__main__":
    main()
