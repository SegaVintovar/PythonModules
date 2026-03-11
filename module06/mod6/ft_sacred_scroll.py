import alchemy
# from alchemy.elements import (
#     create_fire, create_air, create_earth, create_water
#     )


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access")
    print("alchemy.elements.create_fire(): ", alchemy.elements.create_fire())
    print("alchemy.elements.create_water(): ", alchemy.elements.create_water())
    print("alchemy.elements.create_earth(): ", alchemy.elements.create_earth())
    print("alchemy.elements.create_air(): ", alchemy.elements.create_air())
    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_fire(): ", alchemy.create_fire())
        print("alchemy.create_water(): ", alchemy.create_water())
    finally:
        pass
    try:
        print("alchemy.create_earth(): ", alchemy.create_earth())
    except AttributeError as e:
        print(str(e))
    try:
        print("alchemy.create_air(): ", alchemy.create_air())
    except AttributeError as e:
        print(str(e))
    print("\nPackage metadata:")
    print("Version: ", alchemy.__version__)
    print("Author: ", alchemy.__author__)


if __name__ == "__main__":
    main()