from ex0 import Card, Rarity
from ex2 import Combatable
from .Rankable import Rankable


class TournamentCard (Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, id: str, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.id = id
        self.damage = 6
        self.rating = 0
        self.rank = 0
        self.wins = 0
        self.losses = 0
        self.health = health
        self.damage_received = 0
        self.damage_given = 0

    def play(self, game_state: dict) -> dict:
        game_state["mana"] -= self.cost
        actions = {
            "cards_played": self.name,
            "mana_used": 200 - game_state["mana"]
        }
        return actions

    def attack(self, target: Card) -> dict:
        self.damage_given += self.damage
        result = {
            'attacker': self.name, 'target': [t.name for t in target],
            'damage': self.damage, 'combat_type': 'melee'
        }
        return result

    def calculate_rating(self) -> int:
        rarity_value = Rarity[self.rarity.upper()].value
        rating = 1000 + (self.cost * rarity_value)
        return rating

    def get_tournament_stats(self) -> dict:
        stats = {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }
        return stats

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        info = {
            "id": self.id,
            "rank": self.rank
        }
        return info

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
