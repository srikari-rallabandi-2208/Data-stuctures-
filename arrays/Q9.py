#Question :

#rearrange the given list such that the negative numbers are on one side and the positive numbers are on the other side

def rearrange(lst):
    positive = []
    negative = []
    for num in lst :
        if num >= 0 :
            positive.append(num)
        else :
            negative.append(num)
    ans = negative + positive
    return ans