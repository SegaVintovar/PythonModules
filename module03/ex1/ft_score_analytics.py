import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    if argc > 1:
        scores = []
        i = 1
        while i < argc:
            try:
                scores += [int(sys.argv[i])]
            except ValueError:
                print(
                    f"Error: '{sys.argv[i]}' is not an int type"
                    "\nStart the program again with valid input"
                )
                return
            i += 1
        print(f"Scores processed: {scores}")
        total_scores = sum(scores)
        total_players = len(scores)
        print(f"Total players: {total_players}")
        print(f"Total score: {total_scores}")
        avg_score = total_scores / total_players
        print(f"Average score: {avg_score}")
        print(f"High score: {max(scores)}")
        print(f"Lowest score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
        print()
    else:
        print(
            "No scores provided."
            " Usage: python3 ft_score_analytics.py <score1> <score2> .."
        )


if __name__ == "__main__":
    main()
