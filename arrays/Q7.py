#Question :

#find second maximum element of a list

def find_second_max(lst):
    n = len(lst)
    lst.sort()        
    if n > 1 :
        return lst[n-2]