from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    result1 = "Philosopher’s stone created using "
    result2 = f"{lead_to_gold()} and {healing_potion()}"
    return result1 + result2


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
