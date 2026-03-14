from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    # what if every play we are dicreasing game_state["mana"] by mana cost
    # of the card
    @abstractmethod
    def play(self, game_state: dict) -> None:
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
