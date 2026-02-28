import sys


class InputError(Exception):
    def __init__(self, message):
        super().__init__(message)


def parsing(arguments: list) -> dict:
    """
    Here i am creating an invontory that is a dict.
    update() method is used to add new items to my inventory
    """
    result = {}
    i = 1
    while i < len(arguments):
        tmp = arguments[i].split(":")
        if len(tmp) == 2:
            try:
                result.update({tmp[0]: int(tmp[1])})
                i += 1
            except ValueError:
                raise ValueError(
                    "Caught ValueError: The value should be numeric"
                    )
        else:
            raise InputError(
                f"Agrument {tmp} is incorrect!\n"
                "Format should be: program_name iteam:value"
                )
    return result


def inventory_status(inventory: dict) -> None:
    """
    Here I am using get() method to get a value of the item in stock
    """
    total_items = 0
    for value in inventory:
        total_items += inventory.get(value)
    print(f"Total items in inventory: {total_items}")
    unique_items = 0
    for value in inventory:
        unique_items += 1
    print(f"Unique items types: {unique_items}")


def inventory_stats(inventory: dict) -> None:
    """
    Here method items() returns me the keys and values
    """
    print("\n=== Current Inventory ===")
    total_items = 0
    for value in inventory:
        total_items += inventory.get(value)
    largest_item_value = 0
    for key, value in inventory.items():
        percent = 100 * value / total_items
        print(
            f"{key}: {value} units ({percent:.1f}%)"
        )
        if value > largest_item_value:
            largest_item_value = value
            largest_item_name = key
    smallest_item_value = largest_item_value
    for key, value in inventory.items():
        if value < smallest_item_value:
            smallest_item_value = value
            smallest_item_name = key
        if total_items == 1:
            smallest_item_name = largest_item_name
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {largest_item_name} ({largest_item_value} units)")
    print(
        f"Least abundant: {smallest_item_name} ({smallest_item_value} units)"
    )


def categories(inventory: dict) -> None:
    print("\n=== Item Categories ===")
    categorized = {"Moderate": {}, "Scarce": {}}
    for key, value in inventory.items():
        if value > 3:
            categorized["Moderate"][key] = value
        elif value < 4:
            categorized["Scarce"][key] = value
    print(f"Moderate: {categorized['Moderate']}")
    print(f"Scarce: {categorized['Scarce']}")
    print("\n=== Management Suggestions ===")
    to_restock = []
    for key, value in categorized["Scarce"].items():
        if value < 2:
            to_restock += [key]
    print(f"Restock needed: {to_restock}")


def demo(inventory: dict) -> None:
    print("\n=== Dictionary Properties Demo ===")
    inventory_keys = list(inventory.keys())
    inventory_values = list(inventory.values())
    print(f"Dictionary keys: {inventory_keys}")
    print(f"Dictionary values: {inventory_values}")


def finder(inventory: dict, item: str) -> bool:
    if item in inventory:
        return True
    else:
        return False


def inventory_system():
    print("=== Inventory System Analysis ===")
    if (len(sys.argv) > 1):
        try:
            inventory = parsing(sys.argv)
            inventory_status(inventory)
            inventory_stats(inventory)
            categories(inventory)
            demo(inventory)
            item_to_check = "apples"
            print(
                f"Sample lookup - {item_to_check} "
                f"in inventory: {finder(inventory, item_to_check)}"
            )
        except Exception as e:
            print(str(e))
    else:
        print("Fill in the inventory by passing items to the program"
              " items and their amount have to be separated with ':'\n"
              "Example input:\n"
              "python3 ft_inventory_system.py apple:5 bannana:3")


if __name__ == "__main__":
    inventory_system()
