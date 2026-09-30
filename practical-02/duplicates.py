def find_duplicates_brute_force(values):
	"""Return the distinct duplicate elements using pairwise comparisons."""
	duplicates = []

	for index, value in enumerate(values):
		if value in values[index + 1:] and value not in duplicates:
			duplicates.append(value)

	return duplicates



sample = [1, 2, 3, 2, 4, 1, 2]
print(find_duplicates_brute_force(sample))
