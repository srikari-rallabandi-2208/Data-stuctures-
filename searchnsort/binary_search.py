
def binarySearch(lst, low, high, item):
    
    if high >= low:
        mid = (low + high)//2
        
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            return binarySearch(lst, low, mid -1, item)
        else: 
            return binarySearch(lst, mid+1, high,item)
    else:
        return -1

if __name__ == "__main__":
    
    samp = [1,2,3,4,5,6,7,8,9,10]
    
    result = binarySearch(samp,0,len(samp)-1,4)
    
    if result == -1:
        print("search failed")
    else: 
        print(f"element found at {result}")