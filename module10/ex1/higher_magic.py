from typing import Callable, Any


class Spell():
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __call__(self, argumnet: int | None = None) -> int:
        if not argumnet:
            argumnet = 0
        return self.power + argumnet


# spell_combiner(spell1, spell2)- Combine two spells:
# • Return a new function that calls both spells with the same arguments
# • The combined spell should return a tuple of both results
# • Example: combined = spell_combiner(fireball, heal)
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def mixer(argument: Any | None = None) -> tuple:
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


# conditional_caster(condition, spell) - Cast spell conditionally:
# • Return a function that only casts the spell if condition returns True
# • If condition fails, return "Spell fizzled"
# • Both condition and spell receive the same arguments
def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditioned(argumnet: Any) -> int | str:
        if condition(argumnet):
            return spell(argumnet)
        else:
            return "Spell fizzled"
    return conditioned


# spell_sequence(spells) - Create spell sequence:
# • Return a function that casts all spells in order
# • Each spell receives the same arguments
# • Return a list of all spell results
def spell_sequence(spells: list[Callable]) -> Callable:
    def cast(argument: Any) -> list:
        result = []
        for spell in spells:
            result.append(spell(argument))
        return result
    return cast


def condition(x: int) -> bool:
    if x > 0:
        return True
    else:
        return False


def main() -> None:
    print("\nHigh-school magic\n")
    print("<============================>\n")
    my_spell = Spell("spell", 5)
    names = ["spell1", "spell2", "spell3"]
    spells = []
    i = 1
    for spell in names:
        spells.append(Spell(spell, i))
        i += 1
    print("Testing spell combiner:")
    combi = spell_combiner(spells[0], spells[1])
    print("Spell combiner result: ", combi(5))
    print("\nTesting spell amplifier:")
    amp = power_amplifier(spells[2], 2)
    print("Spell amplificator result: ", amp(2))
    # condition = lambda x: x > 0
    # print(callable(condition))
    print("\nTesting conditional caster:")
    cond = conditional_caster(condition, my_spell)
    print("Result of the conditional caster: ", cond(0))
    print("\nTesting spell sequence:")
    seq = spell_sequence(spells)
    print("Spell sequence result: ", seq(2), "\n")
    # print(callable(Spell))
    # print(callable(my_spell))


if __name__ == "__main__":
    main()
