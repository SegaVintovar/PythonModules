from typing import Callable, Any


class Spell():
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __call__(self, multiplier: int) -> None:
        self.power *= multiplier


# spell_combiner(spell1, spell2)- Combine two spells:
# • Return a new function that calls both spells with the same arguments
# • The combined spell should return a tuple of both results
# • Example: combined = spell_combiner(fireball, heal)
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def mixer(argument: Any) -> tuple:
        return (spell1(argument), spell2(argument))
    return mixer


# power_amplifier(base_spell, multiplier)- Amplify spell power:
# • Return a new function that multiplies the base spell’s result by multiplier
# • Assume base spell returns a number (damage, healing, etc.)
# • Example: mega_fireball = power_amplifier(fireball, 3)
def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    base_spell *= multiplier
    return base_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    ...


def spell_sequence(spells: list[Callable]) -> Callable:
    ...


def main() -> None:
    my_spell = Spell("spell", 5)
    print(callable(Spell))
    print(callable(my_spell))


if __name__ == "__main__":
    main()
