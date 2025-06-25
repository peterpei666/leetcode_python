from math import sqrt, ceil

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def prime(x: int) -> bool:
            if x == 2:
                return True
            if x == 1 or x % 2 == 0:
                return False
            for i in range(3, ceil(sqrt(x)) + 1, 2):
                if x % i == 0:
                    return False
            return True
        
        l, r = -1, -1
        for i in range(len(nums)):
            if prime(nums[i]):
                if l == -1:
                    l = i
                r = i
        return r - l
