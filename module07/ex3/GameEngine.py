from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


# Game Orchestrator
class GameEngine():
    def __init__(self) -> None:
        self.factory: CardFactory = None
        self.strategy: GameStrategy = None
        self.turns = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy
            ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        # make factory create a hand
        # add counting for the stats
        deck = self.factory.create_themed_deck(6)
        hand = []
        for value in deck.values():
            for card in value:
                hand.append(card)
        # print("Hand: ", hand)
        print("\nSimulating aggressive turn...\n", "\b",
              "Hand: ", [card.name for card in hand]
              )
        battelfield = self.factory.create_themed_deck(2)
        enemies = []
        for value in battelfield.values():
            for card in value:
                enemies.append(card)
        self.cards_created = len(hand) + len(enemies)
        print("\nTurn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        actions = self.strategy.execute_turn(hand, enemies)
        print("Actions: ", actions)
        self.turns += 1
        self.total_damage += actions["damage_dealt"]
        return actions

    def get_engine_status(self) -> dict:
        result = {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_Created": self.cards_created
        }
        return result
