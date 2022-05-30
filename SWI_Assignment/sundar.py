from random import choices
from collections import Counter


def pick_a_number_from_list(num_list):
	return choices(num_list, weights=num_list, k=1)[0]


def sampling_based_on_magnitude():
	inp, numbers = input('Enter space-separated numbers: '), []
	num_list = [int(i) for i in inp.split()]

	for _ in range(100):
		random_num = pick_a_number_from_list(num_list)
		numbers.append(random_num)
		print(random_num)

	print(f'The freq of numbers is: {Counter(numbers)}')


sampling_based_on_magnitude()
