def garden_operations():
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


def test_error_types():
    """This functions respresents and handles different types of error"""
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
