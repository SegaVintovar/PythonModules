from ex2 import EliteCard, Combatable, Magical
from ex0 import Card


def main() -> None:
    aragorn = EliteCard("Aragorn", 5, "Legendary", 5)
    arc_war = {
        "name": " Arcane Warrior",
        "cost": 5,
        "rarity": "Legendary",
        # "attack": 7,
        "health": 5
        }
    arcane_warrior = EliteCard(**arc_war)
    game_state = {
        "mana": 20,
        "enemy": [arcane_warrior],
        "damage": 3
    }
    print("\n=== DataDeck Ability System ===\n")
    parent_classes = [Card, Combatable, Magical]
    print("EliteCard capabilities:")
    for clas in parent_classes:
        print("- ", clas.get_type(clas), clas.get_methods_list())
    aragorn.play(game_state)
    print()
    print("Multiple interface implementation successful!")
    


if __name__ == "__main__":
    main()
