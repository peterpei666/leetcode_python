class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        odd = 0
        for i in range(n):
            if nums1[i] & 1:
                odd += 1
        valid_odd = True
        valid_even = True
        for i in range(n):
            if nums1[i] & 1:
                valid_even &= odd > 1
            else:
                valid_odd &= odd > 0
        return valid_odd or valid_even
