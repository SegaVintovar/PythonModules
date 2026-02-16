def  check_temperature(temp_str: str):
    try:
        temperature = int(temp_str)
    except ValueError: 
        print(f"Error: {temp_str} in not valid number")
        return None
    else:
        if temperature > 40:
            print(f"Error {temperature}°C is too hot for palnats (max 40°C)")
        elif temperature < 0:
            print(f"Error {temperature}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temperature}°C is perfect for plants!")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    temp = "25"
    print(f"\nTesting temperature: {temp}")
    check_temperature(temp)
    temp = "abc"
    print(f"\nTesting temperature: {temp}")
    check_temperature(temp)
    temp = "100"
    print(f"\nTesting temperature: {temp}")
    check_temperature(temp)
    temp = "-50"
    print(f"\nTesting temperature: {temp}")
    check_temperature(temp)
    print("\nAll tests completed - program didn't crash!")

test_temperature_input()