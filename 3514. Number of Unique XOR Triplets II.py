class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        find = [False] * 2048
        temp = [0]
        find[0] = True
        for i in range(1, n):
            for j in range(i):
                t = nums[i] ^ nums[j]
                if not find[t]:
                    temp.append(t)
                    find[t] = True
        ret = [False] * 2048
        for i in range(n):
            for j in temp:
                ret[nums[i] ^ j] = True
        return sum(ret)
