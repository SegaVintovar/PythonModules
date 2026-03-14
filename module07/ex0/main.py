# from .Card import Card
from . import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:\n", fire_dragon.get_card_info(), "\n")
    # print("Playing Fire Dragon with 6 mana available:")
    game_state = {
        "mana": 6
    }
    print(
        f"Playing {fire_dragon.name} with {game_state['mana']} mana available:"
        )
    print(f"Playable: {fire_dragon.is_playable(game_state['mana'])}")
    print("Play result: ", fire_dragon.play(game_state), "\n")
    goblin_warrior = CreatureCard("Goblin Warrior", 2, "Common", 5, 3)
    attack_result = fire_dragon.attack_target(goblin_warrior)
    print("Attack result: ", attack_result)
    game_state["mana"] = 3
    print(f"\nTesting isufficient mana ({game_state['mana']} avaliable):")
    print("Playable: ", fire_dragon.is_playable(game_state['mana']))
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
