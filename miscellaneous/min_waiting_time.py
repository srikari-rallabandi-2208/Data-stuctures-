'''
AlgoExpert - Minimum waiting time - greedy algorithm
'''

def min_waiting_time(queries):
	queries.sort()
	total_waiting_time = 0
	for idx, duration in enumarate(queries):
		queries_left = len(queries) - (idx + 1)
		total_waiting_time += duration * queries_left
	return total_waiting_time
