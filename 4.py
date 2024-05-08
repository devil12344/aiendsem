from typing import List

class Solution:
    def isSafe(self, row, col, board, n):
        # Check if there is a queen in the same row to the left
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        
        # Check if there is a queen in the upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check if there is a queen in the lower left diagonal
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def solve(self, col, board, ans, n):
        if col == n:
            ans.append(["".join(row) for row in board])
            return
        
        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row][col] = 'Q'
                self.solve(col + 1, board, ans, n)
                board[row][col] = '.'
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans

if __name__ == "__main__":
    s = Solution()
    n = int(input("Enter the n: "))
    result = s.solveNQueens(n)
    for board in result:
        for row in board:
            print(row)
        print()
