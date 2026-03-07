import alchemy
from alchemy.elements import (
    create_fire, create_air, create_earth, create_water
    )


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access")
    print(create_fire())
    print(create_water())
    print(create_earth())
    print(create_air())
    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_fire():", alchemy.create_fire())
        print(alchemy.create_water())
    finally:
        pass
    try:
        print("alchemy.create_earth()", alchemy.create_earth())
    except AttributeError as e:
        print(str(e))
    try:
        print(alchemy.create_air())
    except AttributeError as e:
        print(str(e))
    print("\nPackage metadata:")
    print("Version: ", alchemy.__version__)
    print("Author: ", alchemy.__author__)


if __name__ == "__main__":
    main()