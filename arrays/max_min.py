#Question :

#rearrange the given list such that 0th index has largest , 1st index has smallest , 2nd index has second largest and so on.

def max_min(lst):
    n = len(lst)
    right = n-1
    left = 0
    ans = []
    while right > left :
        ans.append(lst[right])
        ans.append(lst[left])
        right -= 1
        left += 1
    ans.append(lst[(right + left)//2])
    return ans