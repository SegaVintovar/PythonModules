from .elements import (create_air, create_earth, create_fire, create_water)


fire_result = create_fire()
water_result = create_water()
earth_result = create_earth()
air_result = create_air()
two_results = fire_result + "\n" + water_result + "\n"
another_two_results = earth_result + "\n" + air_result
all_four_results = two_results + another_two_results


def healing_potion() -> str:
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    return f"Wisdom potion brewed with all elements: {all_four_results}"
