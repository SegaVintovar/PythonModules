def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    unit_list = ['packets', 'grams', 'area']
    if (unit in unit_list):
        seed_type = seed_type.capitalize()
        if (unit == 'packets'):
            print(seed_type, 'seeds: ', quantity, unit, 'avaliable')
        if (unit == 'grams'):
            print(seed_type, 'seeds: ', quantity, unit, 'total')
        if (unit == 'area'):
            unit = 'sqaure meters'
            print(seed_type, 'seeds: covers', quantity, unit)
    else:
        print('Unknown unit type')
