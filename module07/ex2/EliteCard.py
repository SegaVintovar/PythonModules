from ex0 import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.health = health
        self.mana = 8
        self.damage = 6
        self.damage_received = 0
        self.damage_given = 0
        self.total_mana_spent = 0
        self.total_mana_channeled = 0


    def play(self, game_state: dict) -> None:
        game_state["mana"] -= self.cost
        print("Combat phase:")
        print("Attack result: ", self.attack(game_state["enemy"]))
        print("Defense result: ", self.defend(game_state["damage"]))
        print("\nMagic phase:")
        print(
            "Spell cast: ", self.cast_spell("Fireball", game_state['enemy'])
            )
        print("Mana channel: ", self.channel_mana(self.cost))

    def attack(self, target: list) -> dict:
        result = {
            'attacker': self.name, 'target': [t.name for t in target],
            'damage': self.damage, 'combat_type': 'melee'
        }
        return result

    def defend(self, incoming_damage: int) -> dict:
        self.damage_received += incoming_damage
        damage_blocked = self.health - incoming_damage
        if damage_blocked > 0:
            still_alive = True
        else:
            still_alive = False
        result = {
            'defender': self.name, 'damage_taken': incoming_damage,
            'damage_blocked': damage_blocked,
            'still_alive': still_alive
        }
        return result

    def get_combat_stats(self) -> dict:
        result = {
            "total_damage_dealt": self.damage_given,
            "total_damage_received": self.damage_received
        }
        return result

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = len(targets) * 2
        self.mana -= mana_used
        self.total_mana_spent += mana_used
        result = {
            'caster': self.name, 'spell': spell_name,
            'targets': [t.name for t in targets], 'mana_used': mana_used
        }
        return result

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        self.total_mana_channeled += amount
        result =  {'channeled': amount, 'total_mana': self.mana}
        return result


    def get_magic_stats(self) -> dict:
        return {
            "total_mana_used": self.total_mana_spent,
            "total_mana_channeled": self.total_mana_channeled
        }
