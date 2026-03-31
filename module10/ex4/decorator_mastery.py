from functools import wraps
from typing import Callable, Any
from time import time
# from ..ex3.functools_artifacts import memoized_fibonacci, norm_fibo


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = time()
        result = func(*args, **kwargs)
        print("Time elapsed: ", round(time() - start, 5))
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if kwargs["power"] >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        n = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal n
            try:
                return func(*args, **kwargs)
            except Exception:
                n += 1
                if n > max_attempts:
                    print("Spell failed, retrying...",
                          f"(attempt {n}/{max_attempts})")
                    wrapper(*args, **kwargs)
                else:
                    return "Spell casting failed after: "\
                            f"{max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    # def __init__(self, name: str, )
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        for char in name:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    @spell_timer
    @power_validator(9)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"

@retry_spell(5)
def test_spell() -> None:
    raise Exception


def main() -> None:
    print("\nDecorator Mastery Demo\n")
    guild = MageGuild()
    print("Testing cast_spell with power validation and spel_timer decorators")
    print(guild.cast_spell("fire", power=9))
    print("\nTesting name validator:")
    print(
        "Mage of mages is valid: ", guild.validate_mage_name("Mage of mages"))
    print("123 is valid: ", guild.validate_mage_name("123"))
    print("\nTesting retry spell:")
    print(test_spell())


if __name__ == "__main__":
    main()
