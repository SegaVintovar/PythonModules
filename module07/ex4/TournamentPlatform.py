from .TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self, name):
        self.name = name
        self.cards: list[TournamentCard] = []
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        print(f"\n{card.name} ({card.id}):")
        interfaces = [clas for clas in card.__class__.__mro__]
        print(
            "- Interfaces: ",
            interfaces[1], interfaces[2], interfaces[3]
        )
        card.rating = card.calculate_rating()
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        for card in self.cards:
            if card.id == card1_id:
                player1: TournamentCard = card
        for card in self.cards:
            if card.id == card2_id:
                player2: TournamentCard = card
        if player1.rating > player2.rating:
            winner = player1

            looser = player2
        else:
            winner = player2
            looser = player1
        winner.rating += 16
        winner.wins += 1
        looser.rating -= 16
        looser.losses += 1
        result = {
            "winner": winner.id, "looser": looser.id,
            "winner_rating": winner.rating,
            "looser_rating": looser.rating
            }
        self.matches_played += 1
        return result

    def get_leaderboard(self) -> list:
        self.cards.sort(key=lambda card: card.rating, reverse=True)
        i = 1
        for card in self.cards:
            card.rank = i
            i += 1
        return self.cards

    def generate_tournament_report(self) -> dict:
        i = 0
        total = 0
        for card in self.cards:
            total += card.rating
            i += 1
        avg_rating = total / i
        result = {'total_cards': len(self.cards),
                  'matches_played': self.matches_played,
                  'avg_rating': avg_rating, 'platform_status': 'active'
                  }
        return result

    def rating_get(self, card: TournamentCard) -> int:
        return card.rating


if __name__ == "__main__":
    platform = TournamentPlatform()
    card = TournamentCard("card", 10, "Common", "CARD_001")
    platform.register_card(card)
