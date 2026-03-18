from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class Rarity(Enum):
    COMMON = (0, "common")
    UNCOMMON = (1, "uncommon")
    RARE = (2, "rare")
    LEGENDARY = (3, "legendary")

    def __init__(self, rarity: int, txt: str):
        self.rarity = rarity
        self.text = txt


class Card(ABC):
    _type = "Card"

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    # what if every play we are dicreasing game_state["mana"] by mana cost
    # of the card
    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> Dict:
        # print(
        #     f"Card {self.name}, uses {self.cost} mana, \
        #           has {self.rarity} rarity"
        #     )
        result = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }
        return result

    def is_playable(self, available_mana: int) -> bool:
        if self.cost > available_mana:
            return False
        else:
            return True

    @classmethod
    def get_methods_list(cls) -> list:
        methods_list = [
            method for method in dir(cls)
            if not method.startswith("_")
            ]
        return methods_list

    def get_type(self) -> str:
        return self._type

    def get_mana_cost(self) -> int:
        return self.cost
