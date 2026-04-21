from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        v0, v1 = 0, 1
        for i in range(1, n):
            n0, n1 = 10 ** 9, 10 ** 9
            if nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]:
                n0 = min(n0, v0)
            if nums2[i - 1] < nums1[i] and nums1[i - 1] < nums2[i]:
                n0 = min(n0, v1)
            if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                n1 = min(n1, v0 + 1)
            if nums2[i - 1] < nums2[i] and nums1[i - 1] < nums1[i]:
                n1 = min(n1, v1 + 1)
            v0, v1 = n0, n1
        return min(v0, v1)
