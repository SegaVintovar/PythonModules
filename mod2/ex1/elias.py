X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
B = "\033[94m"
C = "\033[96m"
M = "\033[95m"
Y = "\033[93m"
D = "\033[2m"
H = "\033[1m"

def garden_operations(exception):
    if exception is ValueError:
        i = int("abc")
        print(i)
    if exception is ZeroDivisionError:
        n = 1 / 0
        print(n)
    if exception is FileNotFoundError:
        kaas = open("kaas.txt")
        kaas.close()
    if exception is KeyError:
        d = {"a": 5, "b": 10}
        i = d["c"]
        print(i)


def test_error_types():
    print("=== Garden Error Types Demo ===")
    try:
        print(f"{D}\nTesting ValueError...{X}")
        garden_operations(ValueError)
    except ValueError as e:
        print(f"{R}Caught ValueError: {str(e)}{X}")
    try:
        print(f"{D}\nTesting ZeroDivisionError...{X}")
        garden_operations(ZeroDivisionError)
    except ZeroDivisionError as e:
        print(f"{R}Caught ZeroDivisionError: {str(e)}{X}")
    try:
        print(f"{D}\nTesting FileNotFoundError...{X}")
        garden_operations(FileNotFoundError)
    except FileNotFoundError as e:
        print(f"{R}Caught FileNotFoundError: {str(e)}{X}")
    try:
        print(f"{D}\nTesting KeyError...{X}")
        garden_operations(KeyError)
    except KeyError as e:
        print(f"{R}Caught KeyError: {str(e)}{X}")

    print(f"{D}\nTesting multiple errors together...{X}")
    try:
        n = 1 / int(input(f"{H}What to divide 1 by? "
                          f"(divide by 0 or string) {X}"))
        print(n)
    except (ValueError, ZeroDivisionError):
        print(f"{G}\nCaught an error, but program continues!{X}")


test_error_types()