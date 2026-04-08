from heapq import heappush, heappop

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        def check(k: int) -> bool:
            for i in range(0, n, k):
                block = nums[i : i + k]
                target = sorted_nums[i : i + k]
                if sorted(block) != target:
                    return False
                cnt = 0
                for j in range(k - 1):
                    if block[j] > block[j + 1]:
                        cnt += 1
                if cnt > 1:
                    return False
                if cnt == 1 and block[-1] > block[0]:
                    return False
            return True

        ans = 0
        for k in range(1, n + 1):
            if n % k == 0:
                if check(k):
                    ans += k
        return ans
