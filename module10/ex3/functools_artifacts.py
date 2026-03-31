from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
from datetime import datetime


class MagicEncha():
    def __init__(self, name) -> None:
        self.name = name

    def __call__(self, power, element, target):
        print(
            f"{self.name} targets: {target} with",
            f"{element} and deals {power} damage")


# reduce a list to one value
def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(lambda a, b: a + b, spells)
    if operation == "multiply":
        return reduce(lambda a, b: a * b, spells)
    if operation == "max":
        # return max(spells)
        return reduce(lambda a, b: a if a > b else b, spells)
    if operation == "min":
        # return min(spells)
        return reduce(lambda a, b: a if b > a else b, spells)


# partial creates a new function with some arguments already filled in.
# Take a base enchantment function that needs (power, element, target)
# Adds there element and power, so we need to pass only target  
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": partial(
            base_enchantment, element="fire", power=50
            ),
        "ice_enchant": partial(
            base_enchantment, element="ice", power=50
            ),
        "lightning_enchant": partial(
            base_enchantment, element="lightning", power=50
            )
        }


# Stores previous function results
# If called again with same arguments → returns cached result
# Makes slow recursive functions fast
#
# @lru_cache(maxsize=None): This tells Python to cache every unique result
#  of the function.
# maxsize=None ensures the cache never clears out old results,

# Automatic Lookup: When you call fib_nth(100),
# Python checks if it has the answer in memory first.
# If it does, it returns it instantly without running the recursive math.
# Efficiency: This reduces the time complexity from exponential
#  to linear making it possible to calculate
#  the 100th or 500th term almost instantly.
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


def spell_dispatcher() -> Callable:
    @singledispatch
    def dispatch(data: Any) -> str:
        return f"Unsupported data type {type(data).__name__}"

    @dispatch.register(int)
    def _(data: int) -> str:
        return f"received {data} damage"

    @dispatch.register
    def _(data: str) -> str:
        return f"Enchanted with {data}"

    @dispatch.register
    def _(data: list) -> str:
        return f"received multi-cast - {data}"

    return dispatch


def main() -> None:
    print("Funcools Demo\n")
    spells = [1, 2, 3, 4, 5]
    print(f"Testing spell_reducer with {spells}")
    print("Add: ", spell_reducer(spells, "add"))
    print("Multiply: ", spell_reducer(spells, "multiply"))
    print("Max: ", spell_reducer(spells, "max"))
    print("Min: ", spell_reducer(spells, "min"))
    print("\nTesting partial_enchanter:")
    encha = MagicEncha("someone")
    res = partial_enchanter(encha)
    res["fire_enchant"](target="target")
    res["ice_enchant"](target="target")
    res["lightning_enchant"](target="target")
    print("\nTesting fibonnaci functions:")

    print("memoized_fibonacci(using @lru_cache):")
    begin = datetime.now()
    fibo_data = 40
    print(memoized_fibonacci(fibo_data))
    duration = datetime.now() - begin
    print(f"memoized_fibonacci took this amount of time: {duration}\n")
    print("memoized_fibonacci without @lru_cache:")
    begin = datetime.now()
    print(norm_fibo(fibo_data))
    duration = datetime.now() - begin
    print(
        "memoized_fibonacci without @lru_cache",
        f"took this amount of time: {duration}")
    # print(memoized_fibonacci.cache_info())
    print("\nTesting spell_dispatcher with int, str and list")
    my_dispatched = spell_dispatcher()
    print("int: ", my_dispatched(50))
    print("str: ", my_dispatched("string"))
    print("list: ", my_dispatched(["Fire", "Ice", "Dragon"]))
    print("\nThis is it!")


if __name__ == "__main__":
    main()
