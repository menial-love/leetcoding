from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(temp: List[int],cur: int):
            if cur == len(candidates): return
            if sum(temp) == target:
                res.append(temp[:])
                return
            # 选择同一个数多次
            if sum(temp) + candidates[cur] <= target:
                temp.append(candidates[cur])
                dfs(temp,cur)
                temp.pop()
            elif sum(temp) + candidates[cur] > target: return
            # 选择下一个数
            dfs(temp,cur+1)
        temp=[]
        dfs(temp,0)
        return res
