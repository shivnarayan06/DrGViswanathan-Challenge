class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        state = [-1] * n
        def is_safe(row: int, col: int) -> bool:
            for r in range(row):
                c = state[r]
                if c == col or abs(r - row) == abs(c - col):
                    return False
            return True
        def backtrack(row: int):
            if row == n:
                board = []
                for r in range(n):
                    line = ["."] * n
                    line[state[r]] = "Q"
                    board.append("".join(line))
                ans.append(board)
                return  
            for col in range(n):
                if is_safe(row, col):
                    state[row] = col
                    backtrack(row + 1) 
        backtrack(0)
        return ans