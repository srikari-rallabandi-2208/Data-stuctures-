#Question :

#right rotater the given list by k steps

def right_rotate(lst, k):
    n = len(lst)
    k %= n
    lst[:] = lst[n-k:] + lst[:n-k]
    return lst