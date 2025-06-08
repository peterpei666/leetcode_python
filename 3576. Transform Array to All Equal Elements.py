class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        temp = nums[:]
        cnt1 = 0
        for i in range(len(nums)-1):
            if temp[i] == -1:
                cnt1 += 1
                temp[i+1] *= -1
        if temp[len(nums)-1] == -1:
            cnt1 = float('inf')
        temp = nums[:]
        cnt2 = 0
        for i in range(len(nums)-1):
            if temp[i] == 1:
                cnt2 += 1
                temp[i+1] *= -1
        if temp[len(nums)-1] == 1:
            cnt2 = float('inf')
        return cnt1 <= k or cnt2 <= k
