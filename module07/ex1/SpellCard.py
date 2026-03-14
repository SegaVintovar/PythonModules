from ex0 import Card
from typing import Dict


# Spells are consumed when played (one-time use)
class SpellCard(Card):
    type = "Spell"

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            effect_type: str
            ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> Dict:
        mana = game_state["mana"]
        is_it_playable = self.is_playable(mana)
        if is_it_playable:
            result = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type
            }
            game_state["mana"] -= self.cost
        else:
            result = {"is_playable": is_it_playable}
        return result

    def resolve_effect(self, targets: list) -> Dict:
        return {self.effect_type: targets}
