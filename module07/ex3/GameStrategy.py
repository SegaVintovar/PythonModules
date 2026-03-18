from abc import ABC, abstractmethod


class GameStrategy(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        ...

    @abstractmethod
    def get_strategy_name(self) -> str:
        ...

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        ...
