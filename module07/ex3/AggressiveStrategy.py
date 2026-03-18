from ex0 import Card
from .GameStrategy import GameStrategy

class AggressiveStrategy (GameStrategy):
    _name = "Agressive Strategy"
    def __init__(self):
        pass

    def execute_turn(self, hand: list[Card], battlefield: list) -> dict:
        # sort the hand cards list by cost
        # then execute the turn
        # make game_state for my game
        game_state = {
        "mana": 200,
        "enemy": [battlefield],
        "damage": 3
        }
        # maybe save this data to analyze
        for card in hand:
            print(card.play(game_state))
        print(game_state)
        return game_state

    def get_strategy_name(self) -> str:
        return self._name

    def prioritize_targets(self, available_targets: list) -> list:
        ...

