from typing import List
import queue
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q=queue.Queue()
        col,row=len(image),len(image[0])
        curcolor=image[sr][sc]
        if curcolor == newColor:
            return image
        q.put([sr,sc])
        image[sr][sc]=newColor
        while not q.empty():
            x,y=q.get()
            for tx,ty in [[x,y+1],[x,y-1],[x+1,y],[x-1,y]]:
                if 0 <= tx < col and 0 <= ty < row:
                    if image[tx][ty] == curcolor:
                        q.put([tx,ty])
                        image[tx][ty]=newColor
        return image