class Player():
    def __init__(self, name: str, achivements: set):
        self.name = name
        self.achv = achivements

    def show_achivements(self) -> None:
        print(f"Player {self.name} achivements: {self.achv}")


def achivement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = Player(
        "alice", {
            "first_kill", "level_10", "treasure_hunter", "speed_demon"
        }
    )
    bob = Player(
        "bob", {
            "first_kill", "level_10", "boss_slayer", "collector"
        }
    )
    charlie= Player(
        "charlie", {
            "level_10", "treasure_hunter", "boss_slayer", "speed_demon",
            "perfectionist"
        }
    )
    alice.show_achivements()
    bob.show_achivements()
    charlie.show_achivements()
    all_achives = set(alice.achv | bob.achv | charlie.achv)
    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {all_achives}")
    uniqe_achives = len(set(alice.achv | bob.achv | charlie.achv))
    print(f"Total unique achievements: {uniqe_achives}")
    common = set(alice.achv & bob.achv & charlie.achv)
    print(f"\nCommon to all players: {common}")
    ab = set(alice.achv & bob.achv)
    ac = set(alice.achv & charlie.achv)
    bc = set(bob.achv & charlie.achv)
    duplicates = ab | ac | bc
    rare = all_achives - duplicates
    print(f"Rare achievements (1 player): {rare}")
    print(f"\nAlice vs Bob {alice.achv & bob.achv}")
    print(f"Alice unique {alice.achv - bob.achv}")
    print(f"Bob unique: {bob.achv - alice.achv}")


if __name__ == "__main__":
    achivement_tracker()
