from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    _type = "Combatable"

    @abstractmethod
    def attack(self, target) -> Dict:
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        ...

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        ...

    @classmethod
    def get_methods_list(cls):
        methods_list = [
            method for method in dir(cls)
            if not method.startswith("_")
            ]
        return methods_list

    def get_type(self) -> str:
        return self._type
