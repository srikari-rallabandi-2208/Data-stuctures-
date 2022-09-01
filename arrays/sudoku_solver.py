'''
LeetCode - problem 37
'''

    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        rows = {i: set() for i in range(n)}
        cols = {i: set() for i in range(n)}
        boxes = {(i,j): set() for i in range(3) for j in range(3)}
        
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    rows[i].add(int(board[i][j]))
                    cols[j].add(int(board[i][j]))
                    boxes[(i//3,j//3)].add(int(board[i][j]))
        
        def is_valid(i, j):
            if 0 <= i < n and 0 <= j < n:
                return True
            return False
        
        def get_empty_position():
            for i in range(n):
                for j in range(n):
                    if board[i][j] == '.':
                        return i, j
            return None, None
        
        def dfs():
            i, j = get_empty_position()
            
            if i is None and j is None:
                return True
            
            for num in range(1, 10):
                if num not in rows[i] and num not in cols[j] and num not in boxes[(i//3, j//3)]:
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i//3,j//3)].add(num)
                    board[i][j] = str(num)
                    if dfs():
                        return True
                    
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[(i//3, j//3)].remove(num)
                    
            return False
        
        dfs()
        return board
