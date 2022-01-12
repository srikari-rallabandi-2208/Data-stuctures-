import snoop
import time

#@snoop
def binarySearch(lst, item):
    
    low = 0
    high = len(lst) - 1
    
    while low < high:
        
        mid = (low + high)//2
        
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

if __name__ == "__main__":
    
    samp = [x for x in range(10000)]
    
    start_time = time.perf_counter()
    result = binarySearch(samp,1)
    end_time = time.perf_counter()
    
    print(f"Total time took for binary search: {start_time - end_time:0.7f} seconds ")
    
    if result == -1:
        print("search failed")
    else: 
        print(f"element found at {result}")
    
