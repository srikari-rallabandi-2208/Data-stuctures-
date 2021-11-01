#Question :

#find max sublist sum == kadane's algorithm

def maxsublist_sum(lst):
    for i in range(1, len(lst)):
        if lst[i-1] > 0:
            lst[i] += lst[i-1]
    return max(lst)