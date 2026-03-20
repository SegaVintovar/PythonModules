from ex0 import Card, Rarity
from ex2 import Combatable
from .Rankable import Rankable


class TournamentCard (Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, id: str):
        super().__init__(name, cost, rarity)
        self.id = id
        self.damage = 6
        self.rating = 0
        self.rating_gain_loss = 0
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        game_state["mana"] -= self.cost
        # print("Combat phase:")
        # print("Attack result: ", self.attack(game_state["enemy"]))
        actions = {
            "cards_played": self.name,
            "mana_used": 200 - game_state["mana"]
        }
        return actions
        

    def attack(self, target) -> dict:
        result = {
            'attacker': self.name, 'target': [t.name for t in target],
            'damage': self.damage, 'combat_type': 'melee'
        }
        return result

    def calculate_rating(self) -> int:
        rarity_value = Rarity[self.rarity.strip().upper()].value
        rating = 1000 + (self.cost * rarity_value)
        return rating

    def get_tournament_stats(self) -> dict:
        ...

    def update_wins(self, wins: int) -> None:
        ...

    def update_losses(self, losses: int) -> None:
        ...

    def get_rank_info(self) -> dict:
        ...
    
    def defend(self, incoming_damage: int) -> dict:
        ...

    def get_combat_stats(self) -> dict:
        ...