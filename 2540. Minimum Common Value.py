from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        p1 = 0
        p2 = 0
        while p1 < n1 and p2 < n2:
            while p1 < n1 and p2 < n2 and nums1[p1] < nums2[p2]:
                p1 += 1
            while p1 < n1 and p2 < n2 and nums1[p1] > nums2[p2]:
                p2 += 1
            if p1 < n1 and p2 < n2 and nums1[p1] == nums2[p2]:
                return nums1[p1]
        return -1
