#Question :

#define a function which will take a list and a number as input and 
# return a pair from the list which will add up to the number

def find_sum(lst, k):
    for num in lst :
        if k-num in lst :
            if num < k-num :
                return [num, k-num]
            else :
                return [k-num, num]
    return False