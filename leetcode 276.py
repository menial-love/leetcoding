from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[i for i in range(1,10)]
        res=[]
        def dfs(target: int, cur: int):
            if len(temp) == k and target == 0:
                res.append(temp[:])
                return
            if len(temp) >= k and target != 0: return
            if cur >= 9: return
            for i in range(cur,len(nums)):
                if nums[i] <= target and nums[i] not in temp:
                    temp.append(nums[i])
                else: return
                dfs(target-nums[i],i+1)
                temp.pop()
        temp=[]
        dfs(n,0)
        return res