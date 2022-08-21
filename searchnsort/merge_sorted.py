'''
LeetCode - problem 88
'''

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        for i in range(n):
          nums1[m+i]=nums2[i]
        
        gap = int(math.ceil((m+n)//2))
        
        
        while gap>=1:
          for i in range(gap,m+n):  
            for j in range(i-gap,-1,-gap):
              if nums1[j]>nums1[j+gap]:
                nums1[j+gap],nums1[j]=nums1[j],nums1[j+gap]
              else:
                break
                  
          gap = gap//2
