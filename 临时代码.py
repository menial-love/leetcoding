from typing import List
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.depth=len(board)
        self.width=len(board[0])
        def dfs(x: int, y: int):
            cnt=0
            for i,j in [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]:
                tx,ty=x+i,y+j
                if 0<= tx< self.depth and 0<= ty< self.width:
                    cnt+=(board[tx][ty]=='M') #统计地雷数量
            if cnt!=0:
                board[x][y]=cnt+'0'
                return
            elif cnt==0:
                board[x][y]='B'
            for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]:
                mx,my=x+i,y+j
                if 0 <= mx < self.depth and 0 <= my < self.width and board[mx][my]=='E':
                    dfs(mx,my)
        x1,y1=click
        if board[x1][y1]=='M':
            board[x1][y1]='x'
            return board
        dfs(x1,y1)
        return board
