def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    fake_open = "lost_archive.txt"
    try:
        with open(fake_open) as fake_file:
            print(fake_file.read())
    except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
    finally:
        fake_file.close()
        print("STATUS: Crisis handled, system stable")
    print()
    forbidden_file = "classified_vault.txt"
    try:
        with open(forbidden_file) as no_permission_file:
            print(no_permission_file.read())
    except PermissionError:
            print("RESPONSE: Security protocols deny access")
    finally:
        forbidden_file.close()
        print("STATUS: Crisis handled, security maintained")
    print()
    std_file = "standard_archive.txt"
    try:
        with open(std_file) as file:
            print("SUCCESS: Archive recovered -", file.read())
    except Exception as e:
            print(str(e))
    finally:
        file.close()
        print("STATUS: Normal operations resumed")
    
if __name__ == "__main__":
    main()