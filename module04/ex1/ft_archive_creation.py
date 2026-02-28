# import os


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    sample_txt = (
        "[ENTRY 001] New quantum algorithm discovered\n" +
        "[ENTRY 002] Efficiency increased by 347%\n" +
        "[ENTRY 003] Archived by Data Archivist trainee"
        )
    fd = "new_discovery.txt"
    print(f"Initializing new storage unit: {fd}")
    try:
        file = open(fd, "x")
    except FileExistsError as e:
        print("Caught FileExistsError: ", str(e))
    else:
        print("Storage unit created successfully...")
        print()
        print("Inscribing preservation data...")
        file.write(sample_txt)
        print(sample_txt)
        file.close()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{fd}' ready for long-term preservation.")
    # os.remove(fd)


if __name__ == "__main__":
    main()
