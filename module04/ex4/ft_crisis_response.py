import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    fake_open = "lost_archive.txt"
    try:
        print("CRISIS ALERT: Attempting access to ", fake_open)
        with open(fake_open) as fake_file:
            print(fake_file.read())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix", file=sys.stderr)
    else:
        fake_file.close()
    finally:
        print("STATUS: Crisis handled, system stable")
    print()
    # forbidden_file = "classified_data.txt"
    forbidden_file = BASE_DIR / "classified_data.txt"
    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open(forbidden_file, "r") as no_permission_file:
            print(no_permission_file.read())
    except PermissionError:
        print("RESPONSE: Security protocols deny access", file=sys.stderr)
    else:
        no_permission_file.close()
    finally:
        print("STATUS: Crisis handled, security maintained")
    print()
    # std_file = "/mnt/c/Users/Laptop/study/python/Python_modules/module04/ex4/standard_archive.txt"
    std_file = BASE_DIR / "standard_archive.txt"
    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open(std_file) as file:
            print("SUCCESS: Archive recovered -", file.read())
    except Exception as e:
        print("FAIL: ", str(e), file=sys.stderr)
    else:
        file.close()
    finally:
        print("STATUS: Normal operations resumed")
    
if __name__ == "__main__":
    main()