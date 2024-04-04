# https://leetcode.com/problems/word-search/?envType=daily-question&envId=2024-04-03
directions = [[0,1], [1,0], [0, -1], [-1, 0]]
def dfs(board, row, col, word, index):
    if board[row][col] == word[index]:
        if index == len(word) - 1:
            return True
        store = board[row][col]
        board[row][col] = "#"
        for (dr,dc) in directions:
            nrow, ncol = row + dr, col + dc
            if nrow >= 0 and nrow < len(board) and ncol >= 0 and ncol < len(board[0]):
                if dfs(board, nrow, ncol, word, index + 1):
                    return True
        board[row][col] = store
    return False
            
    
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(board, r, c, word, 0):
                    return True
        return False
        