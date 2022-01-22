import random
import snoop

#@snoop
def partition(lst,low,high):
    
    index = low #hold an anchor to index to interchange at end
    pivot = lst[index] # fix pivot around which the the division happens
    
    while low < high:
        
        #increment low till lst(low) <= pivot
        while low < len(lst) and lst[low] <= pivot:
            low += 1
        
        #decrement high until lst(high) < pivot
        while lst[high] > pivot:
            high -= 1
        
        #exchange lst[low] and lst[high]    
        if low < high:
            lst[low], lst[high] = lst[high], lst[low]

    # exchange pivot element with the high
    lst[high], lst[index] = lst[index], lst[high]
    
    #return the position of pivot
    return high

#@snoop
def kth_smallest_element(array,low,high, k):
    
    # remove corner case 
    if k > high:
        return -1
    
    position = partition(array,low,high)
    
    if position == k-1:
        return array[position]
    if position > k-1:
        return kth_smallest_element(array,low,position,k)
    else:
        return kth_smallest_element(array,position+1,high,k)

if __name__ == '__main__':
    array =     [x for x in range(15)]
    random.shuffle(array)
    print(array)
    kth = kth_smallest_element(array,0,len(array)-1,5)
    print(kth)