from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res=[]
        wordict={word:i for i,word in enumerate(words)}
        for i,word in enumerate(words):
            for j in range(len(word)+1):
                temp1=word[:j]
                temp2=word[j:]
                if temp1[::-1] in wordict and temp2==temp2[::-1] and wordict[temp1[::-1]] != i:
                        res.append([i, wordict[temp1[::-1]]])
                if j>0 and temp2[::-1] in wordict and temp1==temp1[::-1] and wordict[temp2[::-1]] != i:
                        res.append([wordict[temp2[::-1]], i])
        return res

