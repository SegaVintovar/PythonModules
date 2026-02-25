import sys


class InputError(Exception):
    pass


def main() -> None:
    print("=== Command Quest ===")
    argc = len(sys.argv)
    try:
        if argc == 1:
            raise InputError(
                "No arguments provided!\n"
                f"Program name: {sys.argv[0]}"
            )
    except InputError as e:
        print(str(e))
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments recieved: {argc - 1}")
        i = 1
        while i < argc:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {i}")


if __name__ == "__main__":
    main()
