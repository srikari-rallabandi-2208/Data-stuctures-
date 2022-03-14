'''
leetcode problem 1791 - find center of star graph

'''

def findCenter(self, edges):
    return list(set(edges[0]).intersection(set(edges[1])))[0]

