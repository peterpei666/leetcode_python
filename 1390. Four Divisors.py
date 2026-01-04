from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            count = 0
            s = 0
            i = 1
            while i * i <= num:
                if num % i == 0:
                    j = num // i
                    count += 1
                    s += i
                    if not i == j:
                        count += 1
                        s += j
                    if count > 4:
                        break
                i += 1
            if count == 4:
                ans += s
        return ans
