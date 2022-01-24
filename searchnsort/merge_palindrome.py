
def merge_palindrome(array):
    
    count = 0 # count the number of passes
    
    left = 0 # left pointer to the array
    right = len(array) - 1 # right pointer to the array
    
    while left < right:
        
        if array[left] == array[right]:
            left += 1
            right -= 1
            pass # do not count the number as these are palindrome elements
        elif array[left] > array[right]:
            array[right-1] += array[right-1]
            right -= 1
        else:
            array[left+1] = array[left]
            left += 1
        
        count += 1 # increment the count by 1 since we merged either on right or on left
    
    return count

if __name__ == "__main__":
    
    lst = [6,8,1,3,2]
    count = merge_palindrome(lst)
    print(f"passes = {count}")

    lst = [6,8,1,3]
    count = merge_palindrome(lst)
    print(f"passes = {count}")