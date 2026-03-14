from ex0 import Card
from typing import Dict


#  Artifacts remain in play until destroyed
class ArtifactCard(Card):
    type = "Artifact"

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str
            ):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        mana = game_state["mana"]
        is_it_playable = self.is_playable(mana)
        if is_it_playable:
            result = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect
            }
            game_state["mana"] -= self.cost
        else:
            result = {"is_playable": is_it_playable}
        return result

    def activate_ability(self) -> Dict:
        return {"effect_activated": self.effect}
