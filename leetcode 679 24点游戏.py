from typing import List

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        op = ["+", "-", "*", "/"]
        target = 24
        eps = 1e-6

        def solve(nums: List[float]) -> bool:
            if not nums:
                return False
            if len ( nums ) == 1:
                return abs ( nums[0] - target ) < eps
            for i, x in enumerate ( nums ):
                for j, y in enumerate ( nums ):
                    if i != j:
                        newnums = list ()
                    for k, z in enumerate ( nums ):
                        if k != i and k != j:
                            newnums.append ( z )
                    for operator in op:
                        if (operator == '+' or operator == '*') and i > j:
                            continue
                        if operator == '+':
                            newnums.append ( x + y )
                        elif operator == '-':
                            newnums.append ( x - y )
                        elif operator == '*':
                            newnums.append ( x * y )
                        elif operator == '/':
                            if abs ( y ) > eps:
                                newnums.append ( x / y )
                            else:
                                continue
                            if solve ( newnums ):
                                return True
                            newnums.pop ()
            return False

        return solve ( nums )



