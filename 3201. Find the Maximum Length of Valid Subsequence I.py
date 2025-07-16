class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        allodd, alleven = 0, 0
        for i in nums:
            if i & 1:
                allodd += 1
            else:
                alleven += 1
        oddeven, evenodd = 0, 0
        odd = 1
        for i in nums:
            if i & 1 == odd:
                odd ^= 1
                oddeven += 1
        odd = 0
        for i in nums:
            if i & 1 == odd:
                odd ^= 1
                evenodd += 1
        return max(allodd, alleven, oddeven, evenodd)
