from typing import Callable
from functools import reduce, partial, lru_cache, singledispatch
from datetime import datetime


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
# Adds there element and power, so we need to pass only target  
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, element="fire", power=50),
        "ice_enchant": partial(base_enchantment, element="ice", power=50),
        "lightning_enchant": partial(base_enchantment, element="lightning", power=50)
        }


# Stores previous function results
# If called again with same arguments → returns cached result
# Makes slow recursive functions fast
#
# @lru_cache(maxsize=None): This tells Python to cache every unique result
#  of the function.
# maxsize=None ensures the cache never clears out old results,
# which is perfect for Fibonacci.
# Automatic Lookup: When you call fib_nth(100),
# Python checks if it has the answer in memory first.
# If it does, it returns it instantly without running the recursive math.
# Efficiency: This reduces the time complexity from exponential
#  to linear
# , making it possible to calculate the 100th or 500th term almost instantly.
@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# to demo the difference in time(use n=30)
def norm_fibo(n: int) -> int:
    if n < 2:
        return n
    return norm_fibo(n - 1) + norm_fibo(n - 2)

@singledispatch
def spell_dispatcher() -> Callable:
    @singledispatch.
    def _(data)


def main() -> None:
    begin = datetime.now()
    print(memoized_fibonacci(30))
    duration = datetime.now() - begin
    print(f"memo took this amount of time: {duration}")
    begin = datetime.now()
    print(norm_fibo(30))
    duration = datetime.now() - begin
    print(f"norm took this amount of time: {duration}")
    print(memoized_fibonacci.cache_info())


if __name__ == "__main__":
    main()
