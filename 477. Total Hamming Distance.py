class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        bit = [0] * 32
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bit[i] += 1
        total_distance = 0
        for i in range(32):
            total_distance += bit[i] * (n - bit[i])
        return total_distance
