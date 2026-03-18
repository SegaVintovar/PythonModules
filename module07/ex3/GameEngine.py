from .CardFactory import CardFactory
from .GameStrategy import GameStrategy

# Game Orchestrator
class GameEngine ():
    def __init__(self):
        self.factories = []
        self.stragagies = []

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factories.append(factory)
        self.stragagies.append(strategy)

    def simulate_turn(self) -> dict:
        # make factory create a hand
        for strategy in self.stragagies:
            strategy.execute_turn
        ...

    def get_engine_status(self) -> dict:
        ...

