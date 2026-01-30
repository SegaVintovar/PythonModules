def ft_count_harvest_iterative() -> None:
    days = int(input('Days until harvest: '))
    i = 1
    while i < days + 1:
        print('Day', i)
        i += 1
    print('Harvest time!')
