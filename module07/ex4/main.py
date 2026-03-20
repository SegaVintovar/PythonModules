from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard

def main():
    print("\n=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform("name")
    print("\nRegistering Tournament Cards...")
    card1 = TournamentCard("Fire Dragon", 10, "uncommon", "dragon_001")
    card2 = TournamentCard("Ice Wizard ", 8, "common", "wizard_001")
    platform.register_card(card1)
    platform.register_card(card2)
    print("\nCreating tournament match...")
    print("Match result: ", platform.create_match("dragon_001", "wizard_001"))
    leaderboard = platform.get_leaderboard()
    print("\nTournament Leaderboard:")
    i = 1
    for card in leaderboard:
        print(
            f"{i}. {card.name} - ",
            f"Rating: {card.rating} ({card.wins}-{card.losses})"
        )
        i += 1
    print("\nPlatform report:\n", platform.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===\n",
          "All abstract patterns working together harmoniously!")

if __name__ == "__main__":
    main()
