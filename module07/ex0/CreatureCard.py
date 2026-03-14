from . import Card
from typing import Dict


class CreatureCard(Card):
    type = "Creature"

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int
            ):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        mana = game_state["mana"]
        is_it_playable = self.is_playable(mana)

        if is_it_playable:
            result = {
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": "Creature summoned to battlefield"
                }
            game_state["mana"] -= self.cost
        else:
            result = f"The {self.name} in not playable, {mana} mana is \
                  not enough"
        return result

    def get_card_info(self):
        result = super().get_card_info()
        result.update(
            {
                "type": "Creature",
                "attack": self.attack,
                "health": self.health
            }
        )
        return result

    def attack_target(self, target: Card) -> dict:
        print(f"{self.name} attacks {target.name}")
        combat_result = False
        if self.attack > target.health:
            combat_result = True
        result = {
            "attacker'": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": combat_result
        }
        return result
