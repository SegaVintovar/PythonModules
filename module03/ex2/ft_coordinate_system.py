import math
import sys

def dist_measurer(c1: tuple, c2: tuple) -> float:
    bs = ((c2[0]-c1[0])**2 +(c2[1]-c1[1])**2 + (c2[2]-c1[2])**2)
    return math.sqrt(bs)

def parser(coordinate_string: str) -> tuple:
    print("Parsing coordinates:", f'"{coordinate_string}"')
    almost_result = coordinate_string.split(", ")
    if len(almost_result) != 3:
        raise ValueError(
            "Coordinates must be three values: x, y, z"
        )
    result = []
    i = 0
    # for _ in almost_result:
    while i < len(almost_result):
        try:
            result.append(int(almost_result[i]))
        except ValueError:
            raise ValueError(
                "Error parsing coordinates: invalid literal"
                f" for int() with base 10: '{almost_result[i]}'"
                "\nError details- Type: ValueError,"
                f" Args: (invalid literal for int() with base 10:"
                f"  '{almost_result[i]}')"
            )
        i += 1
    return (result[0], result[1], result[2])


def main():
    print("== Game Coordinate System ===\n")
    start_p = (0, 0, 0)
    end_p = (10, 20, 5)
    print(f"Position created: {end_p}")
    dist1 = dist_measurer(start_p, end_p)
    print(f"Distance between {start_p} and {end_p}: {dist1:.2f}\n")
    user_input = "3, 4, 0"
    try:
        user_p = parser(user_input)
        print(f"Parsed position: {user_p}")
    except ValueError as e:
        print(str(e))
    else:
        dist2 = dist_measurer(start_p, user_p)
        print(f"Distance between {start_p} and {user_p}: {dist2:.2f}\n")

    user_input = "abc, def, ghi"
    try:
        user_er_p = parser(user_input)
        print(f"Parsed position: {user_er_p}")
    except ValueError as e:
        print(str(e))
    else:
        dist2 = dist_measurer(start_p, user_er_p)
        print(f"Distance between {start_p} and {user_er_p}: {dist2:.2f}\n")
    print("\nUnpacking demonstration:")
    x, y, z = user_p
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


main()