
def sort_binary_array(lst):
    low = 0
    high = len(lst) - 1
    
    # The loop has to continue till all the elements are exhausted
    while low < high:
        # move in the array till low hits a 1
        while low < high and lst[low] ==0:
            low += 1
        # move in the array till high hits a 0
        while low < high and lst[high] ==1:
            high -= 1
        # if still low < high swap the elements 
        if low < high:
            lst[low], lst[high] = lst[high], lst[low]

    return lst

if __name__ == "__main__":
    
    lst = sort_binary_array([0,1,0,1,1,1,0,0,1,1])
    print (lst)