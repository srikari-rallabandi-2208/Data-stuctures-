'''
This function is to search by making 3 slices out of the given
given array. This might speed the search further if in case the
sample we are searching is large 

'''

import snoop
import time

#@snoop
def ternary_search(low,high,lst,item):
    
    while high >= low:
         
        # Find mid1 and mid2
        mid1 = low + (high-low) // 3
        mid2 = high - (high-low) // 3
 
        # Find mid1 and mid2 and if they match key then return
        if item == lst[mid1]:
            return mid1
        if item == mid2:
            return mid2

        # since item is not found cut the list into parts
        # if it's between low and mid1
        if item < lst[mid1]:
            high = mid1 - 1
        # if it's between mid2 and high'
        elif item > lst[mid2]:
            low = mid2 + 1
        # else it lies between mid1 and mid2    
        else:
            low = mid1 + 1
            high = mid2 - 1
 
    # if not found return marker
    return -1

if __name__ == "__main__":
    
    
    items = [x for x in range(100000)]
    
    start_time = time.perf_counter()
    result = ternary_search(0,99999,items, 300)
    end_time = time.perf_counter()
    
    print(f"Total time took for ternary search: {start_time - end_time:0.7f} seconds ")
    
    if result == -1:
        print("Item Not found .. :( ")
    else:
        print(f"item found at: {result}")
    
    