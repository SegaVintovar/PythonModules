def getdays() -> int:
	return (int(input('Days until harvest: ')))
def ft_count_harvest_recursive(n: int) -> int:
	days = int(input('Days until harvest: '))
	n = 0
	if (days > n):
		print('Day', n)
	n += 1
	ft_count_harvest_recursive()
ft_count_harvest_recursive()
