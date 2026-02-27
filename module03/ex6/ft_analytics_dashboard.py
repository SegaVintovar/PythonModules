players = {
    "alice": 
        {
            "score": 2300, "achivements": 
            [
                "first_kill", "level_10", "treasure_hunter", "speed_demon"
            ]
        },
    "bob": 
        {
            "score": 1800, "achivements": 
            [
                "first_kill", "level_10", "boss_slayer", "collector"
            ]
        },
    "charlie":
        {
            "score": 2150, "achivements":
            [
                "level_10", "treasure_hunter", "boss_slayer", "speed_demon",
                "perfectionist"
            ]
        },
    "diana":
        {
            "score": 2050, "achivemnts":
            [

            ]
        }
}

def main() -> None:
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    high_scores = [player["score"] for player in players.values() if player["score"] > 2000 ]
    print(high_scores)

main()