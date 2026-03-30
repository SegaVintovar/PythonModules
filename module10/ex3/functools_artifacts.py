from typing import Callable
from functools import reduce, partial, lru_cache


class magic_encha():
    def __init__(self, name):
        self.name = name

    def __call__(self, power, element, target):
        print(
            f"{self.name} targets: {target} with {element} and deals {power}")


# reduce a list to one value
def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(lambda a, b:a + b, spells)
    if operation == "multiply":
        return reduce(lambda a, b:a * b, spells)
    if operation == "max":
        return max(spells)
        # return reduce(lambda a, b:a + b, spells)
    if operation == "min":
        return min(spells)
        # return reduce(lambda a, b:a + b, spells)


# partial creates a new function with some arguments already filled in.
# Take a base enchantment function that needs (power, element, target)
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, element="fire", power=50),
        "ice_enchant": partial(base_enchantment, element="ice", power=50),
        "lightning_enchant": partial(base_enchantment, element="lightning", power=50)
        }


# Stores previous function results
# If called again with same arguments → returns cached result
# Makes slow recursive functions fast
@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    ...


def spell_dispatcher() -> Callable:
    ...


def main() -> None:
    ...


if __name__ == "__main__":
    main()
