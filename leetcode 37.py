from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(pos: int):
            nonlocal flag
            if pos == len(space):
                flag = True
                return
            n, m = space[pos]
            for digit in range(1, 10):
                if line[n][digit] == col[m][digit] == block[n // 3][m // 3][digit] == False:
                    line[n][digit] = col[m][digit] = block[n // 3][m // 3][digit] = True
                    board[n][m] = str(digit)
                    dfs(pos+1)
                    line[n][digit] = col[m][digit] = block[n // 3][m // 3][digit] = False
                if flag:
                    break
        line = [[False] * 10 for _ in range(9)]
        col = [[False] * 10 for _ in range(9)]
        block = [[[False] * 10 for _ in range(3)] for _1 in range(3)]
        space = []
        flag = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.': space.append((i, j))
                else:
                    tempo = int(board[i][j])
                    line[i][tempo] = col[j][tempo] = block[i//3][j//3][tempo] = True
        dfs(0)