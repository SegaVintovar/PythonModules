from typing import Callable, Any


def mage_counter() -> Callable:
    counter = 0

    def cnt() -> int:
        nonlocal counter
        counter += 1
        return counter
    return cnt


def spell_accumulator(initial_power: int) -> Callable:
    battery = initial_power

    def input(power: int):
        nonlocal battery
        battery += power
        return battery
    return input


def enchantment_factory(enchantment_type: str) -> Callable:
    my_type = enchantment_type

    def copulation(name: str) -> str:
        nonlocal my_type
        my_type += name
        return my_type
    return copulation


# memory_vault works without nonlocal
# because dictionary mutation is allowed through closure references.
# also flake8 argue on it
def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        # nonlocal memory
        memory[key] = value

    def recall(key: str) -> Any | str:
        # nonlocal memory
        if key in memory:
            return memory.get(key)
        else:
            return "Memory not found"

    return {
            "store": store,
            "recall": recall
        }


def main() -> None:
    count = mage_counter()
    another_count = mage_counter()
    count()
    count()
    print(count())
    print(another_count)
    vault = memory_vault()
    vault["store"]("key", "value")
    print(vault)
    print(vault["recall"]("key"))


if __name__ == "__main__":
    main()
