'''
AlgoExpert - Tandem Bicycles - greedy algorithm
'''

def tandemBicycle(rss, bss, fastest):
	rss.sort()
	bss.sort()
	
	if not fastest:
		raip(rss)
	
	ts = 0
	for idx in range(len(rss)):
		r1 = rss[idx]
		r2 = bss[len(bss) - idx - 1]
		ts += max(r1, r2)
	return ts

def raip(array):
	start = 0
	end = len(array) - 1
	while start < end:
		array[start], array[end] = array[end], array[start]
		start += 1
		end -= 1
