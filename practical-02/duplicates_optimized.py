def find_duplicates(values):
	"""Return distinct duplicates in their first-seen order."""
	seen = set()
	duplicate_values = set()

	for value in values:
		if value in seen:
			duplicate_values.add(value)
		else:
			seen.add(value)

	duplicates = []
	returned = set()
	for value in values:
		if value in duplicate_values and value not in returned:
			duplicates.append(value)
			returned.add(value)

	return duplicates


sample = [1, 2, 3, 2, 4, 1, 2]
print(find_duplicates(sample))