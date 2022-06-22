'''
AlgoExpert - Bubble Sort - Search and Sort
'''

def bubbleSort(array):
	is_sorted = False
	counter = 0
	while not is_sorted:
		is_sorted = True
		for i in range(len(array) - 1 - counter):
			if array[i] > array[i + 1]:
				swap(i, i , array)
				is_sorted = False
		counter += 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
