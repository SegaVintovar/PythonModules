from abc import ABC, abstractmethod


class Magical(ABC):
    _type = "Magical"

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass

    @classmethod
    def get_methods_list(cls):
        methods_list = [
            method for method in dir(cls)
            if not method.startswith("_")
            ]
        return methods_list

    def get_type(self) -> str:
        return self._type
