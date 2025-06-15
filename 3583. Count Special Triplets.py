from collections import defaultdict
import bisect

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        list1 = defaultdict(list)
        for i in range(len(nums)):
            list1[nums[i]].append(i)
        ans = 0
        for i in range(len(nums)):
            temp = nums[i] * 2
            if temp in list1:
                m = bisect.bisect_left(list1[temp], i)
                n = len(list1[temp]) - bisect.bisect_right(list1[temp], i)
                ans += m * n
                ans %= 10**9 + 7
        return ans
