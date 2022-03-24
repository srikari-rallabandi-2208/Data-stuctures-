'''
leetcode problem 856 - Score of parentheses
'''

def scoreOfParentheses(self, S):
	return eval(S.replace(')(',')+(').replace('()','1').replace(')',')*2'))
	
