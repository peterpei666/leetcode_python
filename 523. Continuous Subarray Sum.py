class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        list = dict()
        list[0] = -1
        cur=0
        for i in range(len(nums)):
            cur += nums[i]
            cur%=k
            if cur in list:
                if i - list[cur] > 1:
                    return True
            else:
                list[cur] = i
        return False
