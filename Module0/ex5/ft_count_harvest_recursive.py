def ft_count_harvest_recursive(n: int) -> None:
	days = int(input('Days until harvest: '))
	n = 1
	def counter(n: int) -> None:
		print ('Day ', n)
		n += 1
	if (days >= n):
		counter(n)
	print ('Harvest time!')
	ft_count_harvest_recursive()
ft_count_harvest_recursive()
