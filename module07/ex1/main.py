from ex0 import CreatureCard
from ex1 import ArtifactCard, Deck, SpellCard


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    game_state = {
        "mana": 20
    }
    ideck = Deck()
    bolt = SpellCard("Lightning Bolt", 3, "Common", "damage")
    crystal = ArtifactCard(
        "Mana Crystal", 2, "Common", 5, "Permanent: +1 mana per turn"
        )
    drago = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    ideck.add_card(bolt)
    ideck.add_card(crystal)
    ideck.add_card(drago)
    print("Deck stats: ", ideck.get_deck_stats())
    ideck.shuffle()
    print("\nShuffeling, Drawing and playing cards:\n")
    card1 = ideck.draw_card()
    print("Drew: ", card1.name, f"({card1.type})")
    print("Play result: ", card1.play(game_state))
    print()
    card2 = ideck.draw_card()
    print("Drew: ", card2.name, f"({card2.type})")
    print("Play result: ", card2.play(game_state))
    print()
    card2 = ideck.draw_card()
    print("Drew: ", card2.name, f"({card2.type})")
    print("Play result: ", card2.play(game_state))
    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
