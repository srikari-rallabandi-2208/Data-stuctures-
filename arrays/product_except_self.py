#Question :

#given a list , define a function that returns a list with product of all numbers in the list except itself

def productExceptSelf(lst):
    p = 1
    n = len(lst)
    output = []
    for i in range(0,n):
        output.append(p)
        p = p * lst[i]
    p = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i] * p
        p = p * lst[i]
    return output