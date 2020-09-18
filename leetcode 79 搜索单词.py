from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dic=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(startx: int, starty: int, k) -> bool:
            for x,y in dic:
                newx,newy=startx+x,starty+y
                if 0 <= newx < len(board[0]) and 0 <= newy < len(board):
                    if k == len(word)-1 and board[newx][newy] == word[k]: return True
                    if board[newx][newy] == word[k]:
                        if dfs(newx,newy,k+1): return True
                    else:continue
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,1): return True
        return False