from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        return any(all(nums[i] > nums[i - 1] for i in range(idx + 1, idx + k)) & all(nums[i] > nums[i - 1] for i in range(idx + k + 1, idx + 2 * k)) for idx in range(0, len(nums) - 2 * k + 1))
