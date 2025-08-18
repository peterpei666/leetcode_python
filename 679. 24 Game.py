from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        nums = []
        dif = 10 ** -6
        for i in cards:
            nums.append(float(i))
        
        def compute(a: float, b: float) -> List[float]:
            ans = [a + b, a - b, b - a, a * b]
            if a > dif:
                ans.append(b / a)
            if b > dif:
                ans.append(a / b)
            return ans
        
        def dfs(nums: List[float]) -> bool:
            n = len(nums)
            if n == 1:
                return abs(nums[0] - 24.0) < dif
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    next = []
                    for k in range(n):
                        if k != i and k != j:
                            next.append(nums[k])
                    for val in compute(nums[i], nums[j]):
                        next.append(val)
                        if dfs(next):
                            return True
                        next.pop()
            return False

        return dfs(nums)        
