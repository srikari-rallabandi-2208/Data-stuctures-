'''
Walmart labs question
'''
def min_jumps(lis):
    ones = []
    jumps, median, index = 0, 0, 0
    n = len(lis)

    for i in range(n):
        if(lis[i] == 1):
            ones.append(i)

    m = len(ones)

    if(m == 0):
        return jumps
 
    median = ones[m // 2]
    index = median
 
    for i in range(index, -1, -1):
        if(lis[i] == 1):
            jumps += index - i
            index -= 1
 
    index = median
 
    for i in range(index, n):
        if(lis[i] == 1):
            jumps += i - index
            index += 1
 
    return jumps

a = [0, 1, 1, 0, 1, 0, 0, 0, 1]
print(min_jumps(a))

b = [1, 0, 1, 0, 1, 0, 1, 0]
print(min_jumps(b))

c = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0]
print(min_jumps(c))
