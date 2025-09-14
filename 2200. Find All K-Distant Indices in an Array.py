class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        valid = [False] * 1000
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                    valid[j] = True
        ret = []
        for i in range(1000):
            if valid[i]:
                ret.append(i)
        return ret
