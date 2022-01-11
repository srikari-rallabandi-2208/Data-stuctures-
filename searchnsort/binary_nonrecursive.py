import snoop

@snoop
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
    
    samp = [1,2,3,4,5,6,7,8,9,10]
    
    result = binarySearch(samp,100)
    
    if result == -1:
        print("search failed")
    else: 
        print(f"element found at {result}")
    
