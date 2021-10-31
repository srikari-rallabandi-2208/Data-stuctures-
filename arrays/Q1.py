#Question :

#remove all even numbers in a given list

def remove_even(lst):
    out = []
    for num in lst:
        if num % 2 == 1:
            out.append(num)
    return out
