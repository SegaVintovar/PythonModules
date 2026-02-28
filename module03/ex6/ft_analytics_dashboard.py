def my_players() -> dict:
    players = {
        "alice":
            {
                "score": 2300,
                "status": "active",
                "region": "east",
                "achivements":
                [
                    "first_kill", "level_10", "treasure_hunter", "speed_demon"
                ]
            },
        "bob":
            {
                "score": 1800,
                "status": "active",
                "region": "north",
                "achivements":
                [
                    "first_kill", "level_10", "boss_slayer"
                ]
            },
        "charlie":
            {
                "score": 2150,
                "status": "active",
                "region": "central",
                "achivements":
                [
                    "level_10", "treasure_hunter", "boss_slayer",
                    "speed_demon",
                    "perfectionist",
                    "collector"
                ]
            },
        "diana":
            {
                "score": 2050,
                "status": "not_active",
                "region": "",
                "achivements":
                [
                    "first_kill", "collector", "perfectionist"
                ]
            }
    }
    return players


def comph_list(players: dict) -> None:
    print("=== List Comprehension Examples ===")
    high_scores = [
        player for player in players
        if players[player]["score"] > 2000
        ]
    print("High scorers (>2000): ", high_scores)
    doubled_scores = [
        players[player]["score"] * 2 for player in players
    ]
    print(f"Scores doubled: {doubled_scores}")
    active_players = [
        player for player in players
        if players[player]["status"] == "active"
    ]
    print(f"Active players: {active_players}")


def comph_dict(players: dict) -> None:
    print("=== Dict Comprehension Examples ===")
    player_scores = {
        player: players[player]["score"] for player in players
        if players[player]["status"] == "active"
    }
    print(f"Active player scores: {player_scores}")
    score_categories = {
        "high": len
        (
                [
                    player for player in players
                    if players[player]["score"] > 2200
                ]
        ),
        "medium": len
        (
            [
                player for player in players
                if players[player]["score"] < 2200
                and players[player]["score"] > 2000
            ]
        ),
        "low": len(
            [
                player for player in players
                if players[player]["score"] <= 2000
            ]
        )
    }
    print(f"Score categories: {score_categories}")
    achv_count = {
        player: len(players[player]["achivements"]) for player in players
        if players[player]["status"] == "active"
    }
    print(f"Achivement counts: {achv_count}")


def comph_set(players: dict) -> set:
    print("\n=== Set Comprehension Examples ===")
    unique_players = {player for player in players}
    print(f"Unique players: {sorted(unique_players)}")
    unique_achv = {
        achivenment for player in players
        for achivenment in players[player]["achivements"]
        }
    print("Unique achievements:", unique_achv)
    bob_achv = {achivement for achivement in players["bob"]["achivements"]}
    print(f"Bob`s achivements: {bob_achv}")
    active_regions = {
        players[player]["region"] for player in players
        if players[player]["status"] == "active"
    }
    print("Active regions: ", active_regions)
    return unique_achv


def combi(players: dict, unique_achv: set) -> None:
    print("\n=== Combined Analysis ===")
    total_players = len({player for player in players})
    print("Total players: ", total_players)
    total_unique_achvs = len(unique_achv)
    print("Total unique achievements: ", total_unique_achvs)
    all_scores = [
        players[player]["score"] for player in players
    ]
    avg_score = sum(all_scores) / len(all_scores)
    print("Average score: ", avg_score)
    best_score = 0
    for player in players:
        if players[player]["score"] > best_score:
            best_score = players[player]["score"]
            best_player = player
            achv_amnt = len(players[player]["achivements"])
    print(
        f"Top performer: {best_player} ({best_score} points, "
        f"{achv_amnt} achievements)"
    )


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    players = my_players()
    comph_list(players)
    print()
    comph_dict(players)
    unique_achv = comph_set(players)
    combi(players, unique_achv)


if __name__ == "__main__":
    main()
