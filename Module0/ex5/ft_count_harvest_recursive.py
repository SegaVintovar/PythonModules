def ft_count_harvest_recursive(days = 0, n = 0) -> None:
	if n == 0:
		days = int(input('Days until harvest: '))
	n += 1
	print('Day ', n)
	if (n == days):
		return (print('Harvest time!'))
	ft_count_harvest_recursive(days, n)
