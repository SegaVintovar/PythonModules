from ex0 import Card
import random
from typing import Dict


class Deck():
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> None:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return
        print(f"{card_name} not found in the stack")

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        top_card: Card = self.cards[0]
        self.cards.pop(0)
        return top_card

    def get_deck_stats(self) -> Dict:
        result = {
            "total": 0,
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0
        }
        result["total"] = len(self.cards)
        total_cost = 0
        for card in self.cards:
            if card.type == "Creature":
                result["creatures"] += 1
            if card.type == "Spell":
                result["spells"] += 1
            if card.type == "Artifact":
                result["artifacts"] += 1
            total_cost += card.cost
        result["avg_cost"] = round((total_cost / result["total"]), 1)
        return result
