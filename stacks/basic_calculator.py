'''
LeetCode - problem 224
'''

    def calculate(self, s: str) -> int:

        res = 0
        num = 0
        operator = '+'
        stack = ['+'] 
        
        def execute_operator(stack, operator, num):
            current_status = stack[-1]
            if operator == current_status:   
                temp = num
            else:
                temp = -num
            return temp
        
        def calculate_current_substring_status(stack, operator):
            current_status = stack[-1]
            if operator == current_status: 
                temp = '+'
            else:
                temp = '-'
            return temp
        
        for char in s+"+":
            if char == ' ':
                continue
            elif char.isdigit():
                num = 10*num + int(char)
            elif char in "+-":
                res += execute_operator(stack, operator, num)
                operator = char
                num = 0
            elif char == "(":
                stack.append(calculate_current_substring_status(stack,operator))
                operator = '+'
            elif char == ")":
                res += execute_operator(stack, operator, num)
                num = 0
                stack.pop()
        return res
