from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def dfs(start: int):
            if start >= len(candidates): return
            if sum(temp) == target:
                res.append(temp[:])
                return
            if sum(temp) + candidates[start] <= target:
                temp.append(candidates[start])
                dfs(start+1) #搜索下一个数
                temp.pop()
            else: return
        temp=[]
        dfs(0)
        return res