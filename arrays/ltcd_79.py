'''
LeetCode - problem 79
'''

def dfs(board, word, r, c, visited):
    if not word:
        return True

    if (
        (r, c) in visited
        or r < 0
        or r >= len(board)
        or c < 0
        or c >= len(board[0])
        or board[r][c] != word[0]
    ):
        return False

    return (
        dfs(board, word[1:], r + 1, c, visited + [(r, c)])
        or dfs(board, word[1:], r - 1, c, visited + [(r, c)])
        or dfs(board, word[1:], r, c + 1, visited + [(r, c)])
        or dfs(board, word[1:], r, c - 1, visited + [(r, c)])
    )

def exist(self, board, word):
    for r, row in enumerate(board):
        for c, l in enumerate(row):
            if dfs(board, word, r, c, []):
                return True
    return False
