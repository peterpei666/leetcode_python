class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        odd = 10 ** 9
        for i in range(n):
            if nums1[i] & 1:
                odd = min(odd, nums1[i])
        valid_odd = True
        valid_even = True
        for i in range(n):
            if nums1[i] & 1:
                valid_even &= nums1[i] > odd
            else:
                valid_odd &= nums1[i] > odd
        return valid_odd or valid_even
