from typing import Callable, Any


class Spell():
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def __call__(self, argumnet: int) -> int:
        return self.power + argumnet


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
    def multiplicator(argument: int) -> int:
        return base_spell(argument) * multiplier
    return multiplicator


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditioned(argumnet: Any) -> int | str:
        if condition(argumnet):
            return spell(argumnet)
        else:
            return "Spell fizzled"
    return conditioned


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast(argument: Any) -> list:
        result = []
        for spell in spells:
            result.append(spell(argument))
        return result
    return cast


def main() -> None:
    my_spell = Spell("spell", 5)
    names = ["spell1", "spell2", "spell3"]
    spells = []
    i = 1
    for spell in names:
        spells.append(Spell(spell, i))
        i += 1
    combi = spell_combiner(spells[0], spells[1])
    print(combi(1))
    amp = power_amplifier(spells[2], 2)
    print(amp(2))
    condition = lambda x: x > 0
    print(callable(condition))
    cond = conditional_caster(condition, my_spell)
    print(cond(0))
    seq = spell_sequence(spells)
    print(seq(2))
    # print(callable(Spell))
    # print(callable(my_spell))


if __name__ == "__main__":
    main()
