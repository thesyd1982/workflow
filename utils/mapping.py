def mapping(target, destination):
	keys_to_map = []
	mapped_keys = []

	target = sorted(target)
	destination = sorted(destination)

	for key in target:
		is_mapped = False
		while not is_mapped and key in destination:
			mapped_keys.append(key)
			is_mapped = True
		if not is_mapped:
			keys_to_map.append(key)

	print(target, destination)

	print('keys to map')
	for key in keys_to_map:
		choix = input('choix clé \n')
		while choix in mapped_keys:
			print(f'{key} déja mappé')
			choix = input('choix clé \n')
		mapped_keys.append(choix)

	print(mapped_keys)


if __name__ == '__main__':
	mapping(["a", "1", "b", "c"], ["a", "c", "d"])
