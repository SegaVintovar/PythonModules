import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    print("Input Stream active.", end=" ")
    id = input("Enter archivist ID: ")
    print("Input Stream active.", end=" ")
    status = input("Enter status report: ")
    print()
    print(f"[STANDARD] Archive status from {id}: {status}", file=sys.stdout)
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr
        )
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
