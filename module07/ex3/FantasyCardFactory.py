from .CardFactory import CardFactory
from ex0 import Card, CreatureCard
from ex1 import ArtifactCard, SpellCard
from random import choice

# FantasyCardFactory.py - Concrete factory:
# • Creates fantasy-themed creatures (Dragons, Goblins, etc.)
# • Creates elemental spells (Fire, Ice, Lightning)
# • Creates magical artifacts (Rings, Staffs, Crystals)
# • Supports extensible card type registration


class FantasyCardFactory(CardFactory):
    def __init__(self, name):
        self.name = name
        self.creatures = [
            {
                "name": "Fire Dragon", "cost": 5,
                "rarity": "Legendary", "attack": 7, "health": 5
            },
            {
                "name": "Goblin Warrior", "cost": 2,
                "rarity": "Common", "attack": 2, "health": 1
            },
            {
                "name": "Stone Golem", "cost": 6,
                "rarity": "Rare", "attack": 5, "health": 8
            }
        ]
        self.articats = [
            {
                "name": "Mana Crystal",
                "cost": 2, "rarity": "Common", "durability": 5,
                "effect": "Permanent: +1 mana per turn"
            },
            {
                "name": "Sword of Power", "cost": 3,
                "rarity": "Uncommon", "durability": 3,
                "effect": "Permanent: +2 attack to equipped creature"
            },
            {
                "name": "Ring of Wisdom", "cost": 4,
                "rarity": "Rare", "durability": 4,
                "effect": "Permanent: Draw an extra card each turn"
            },
            {
                "name": "Staff of Elements", "cost": 6,
                "rarity": "Legendary", "durability": 7,
                "effect": "Permanent: +1 spell damage"
            }
        ]
        self.spells = [
            {"name": "Lightning Bolt", "cost": 3,
             "rarity": "Common", "effect_type": "damage"},
            {"name": "Fireball", "cost": 4,
             "rarity": "Uncommon", "effect_type": "damage"},
            {"name": "Ice Shard", "cost": 2,
             "rarity": "Common", "effect_type": "damage"}
        ]

    def create_card(
            self,
            card_type: Card,
            name_or_power: str | int | None = None,
            ) -> Card:
        source = None
        if card_type == CreatureCard:
            source = self.creatures
        if card_type == SpellCard:
            source = self.spells
        if card_type == ArtifactCard:
            source = self.articats
        if name_or_power:
            for card in source:
                power = card["attack"] + card["health"]
                if card["name"] == name_or_power:
                    result = card_type(**card)
                    return result
                if power >= name_or_power:
                    result = card_type(**card)
                    return result
            print("Not found by name or power")
        else:
            result = choice(source)
            # print(result)
            result = card_type(**result)
            return result

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        return self.create_card(CreatureCard, name_or_power)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        return self.create_card(SpellCard, name_or_power)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        return self.create_card(ArtifactCard, name_or_power)

    def create_themed_deck(self, size: int) -> dict:
        i = 0
        deck = {
            "creature_cards": [],
            "spell_cards": [],
            "artifacts": []
        }
        while i < size:
            if i % 3 == 0:
                deck["creature_cards"].append(self.create_creature())
            elif i % 2 == 0:
                deck["spell_cards"].append(self.create_spell())
            else:
                deck["artifacts"].append(self.create_artifact())
            i += 1
        return deck

    def get_supported_types(self) -> dict:
        result = {
            "creatures": [creature["name"] for creature in self.creatures],
            "spells": [spell["name"] for spell in self.spells],
            "artifacts": [artifact["name"] for artifact in self.articats]
        }
        return result


if __name__ == "__main__":
    test = FantasyCardFactory("test")
    print(test.create_creature())
