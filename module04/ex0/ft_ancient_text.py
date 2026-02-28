def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        fd = "ancient_fragment.txt"
        print(f"\nAccessing Storage Vault: {fd}")
        with open(fd) as file:
            print("Connection established...\n")
            print(file.read())
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("FileNotFoundError")


if __name__ == "__main__":
    main()
