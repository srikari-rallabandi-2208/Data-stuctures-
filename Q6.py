#Question :

#find the first unique element in the list

def solution(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for item in lst:
        if counts[item] == 1:
            return item
    return -1