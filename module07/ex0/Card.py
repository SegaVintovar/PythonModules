from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> None:
        pass

    def get_card_info(self) -> None:
        print(
            f"Card {self.name}, uses {self.cost} mana, \
                  has {self.rarity} rarity"
            )

    def is_playable(self, available_mana: int) -> bool:
        if self.cost > available_mana:
            return False
        else:
            return True
