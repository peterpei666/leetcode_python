import bisect

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n2 = len(nums2)
        def count(target: int) -> int:
            cnt = 0
            for i in nums1:
                if i > 0:
                    cnt += bisect.bisect_right(nums2, target // i)
                elif i < 0:
                    f = target // i
                    if target % i:
                        f += 1
                    cnt += n2 - bisect.bisect_left(nums2, f)
                else:
                    if target >= 0:
                        cnt += n2
            return cnt
        
        l, r = - 10 ** 10, 10 ** 10
        while l < r:
            mid = l + (r - l) // 2
            if count(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l
