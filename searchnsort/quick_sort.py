import random
import unittest

def partition(start,end,lst):
    
    index = start # Keep track of the index so that you can exchange it with the end
    pivot = lst[index] # value around which your array would be partitioned
    
    # loop though till the start and end doesn't cross
    while start < end:
        
        # move start pointer while it's less than pivot
        while start < len(lst) and lst[start] <= pivot:
            start += 1
            
        #move the end pointer till it's greater than pivot'
        while lst[end] > pivot:
            end -= 1
        
        # if the start and end does,'t cross it means that there are elements
        # in between who are not sorted. Hence exchange start and end 
        if start < end:
            lst[start],lst[end] = lst[end],lst[start]
    
    # once we are out of the loop exchange pivot and end
    # by this we fix the location of the pivot and
    # by now all the elements that are less than pivot are on left side of pivot
    # all the elements that are greater than pivot are on the right side.
    lst[end],lst[index] = lst[index],lst[end]
    
    # return pivot position
    return end
    

def quick_sort(start, end, lst):
    
    if start < end:
        # partition the array
        part = partition(start,end,lst)
        
        # call quick_sort on the left partition
        quick_sort(start, part-1,lst)
        # call quick_sort on the right partition
        quick_sort(part+1, end, lst)


class QSTest(unittest.TestCase):
    
    def test_quick_sort(self):
        array =     [x for x in range(100)]
        initial_array = array
        random.shuffle(array)
        print(array)
        quick_sort(0,len(array)-1, array)
        print(f"Sorted Array {array}")
        self.assertEqual(initial_array,array,"Array didn't sort !")

if __name__ == "__main__":
    
    unittest.main()