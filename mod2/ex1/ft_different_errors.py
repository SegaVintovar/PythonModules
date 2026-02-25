# def garden_operations() -> None:
#     """This function demostrates errors that can occure.
#     It handles them
#     THe intrepetruer will not stop execution as soon as first error
#     will occure"""

#     temp_str = "abc"
#     # Value error
#     try:
#         temperature = int(temp_str)
#     except ValueError as e:
#         print(str(e))
#     else:
#         print(temperature)
#     # ZeroDivision error
#     temperature = 1
#     try:
#         infinity = temperature / 0
#     except ZeroDivisionError as e:
#         print(str(e))
#     else:
#         print(infinity)
#     # FileNotFoundError
#     fd = "missing.txt"
#     try:
#         missing = open(fd)
#     except FileNotFoundError as e:
#         print(str(e))
#     finally:
#         missing.close()
#     # KeyError
#     test = {"name": "Valentyn", "surname": "Sudak"}
#     try:
#         print(test["age"])
#     except KeyError as e:
#         print(str(e))


def garden_operations() -> None:
    """This function demostrates errors that can occure.
    It does not handle them
    THe intrepetruer will stop execution as soon as first error
    will occure"""
    temp_str = "abc"
    # Value error
    temperature = int(temp_str)
    # ZeroDivision error
    temperature = 1
    infinity = temperature / 0
    print(infinity)
    # FileNotFoundError
    fd = "missing.txt"
    missing = open(fd)
    missing.close()
    # KeyError
    test = {"name": "Valentyn", "surname": "Sudak"}
    print(test["age"])


def test_error_types() -> None:
    """
    This functions respresents and handles different types of error
    """
    print("=== Garden Error Types Demo ===")
    temp_str = "abc"
    try:
        temperature = int(temp_str)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    temperature = 1
    try:
        reuslt = temperature / 0
        print(reuslt)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    fd = "missing.txt"
    try:
        open(fd)
    except FileNotFoundError:
        print("Caught FileNotFoundError: ",
              "No such file or directory: 'missing.txt'")
    test = {"name": "Valentyn", "surname": "Sudak"}
    try:
        test["age"]
    except KeyError:
        print("Caught KeyError: 'age'")
    print("\nTesting multiple errors together...")
    test = {"error": "string", "zero": 0}
    try:
        number = int(test["error"])
        division = number / test["zero"]
        print(division)
    except (ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")
