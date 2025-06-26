from sortedcontainers import SortedList

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = SortedList(nums1)
        ret = [0] * len(nums1)
        nums = sorted([(b, i) for i, b in enumerate(nums2)])
        for b, i in nums:
            id = mp.bisect_right(b)
            if id < len(mp):
                ret[i] = mp[id]
                mp.pop(id)
            else:
                ret[i] = mp[0]
                mp.pop(0)
        return ret
