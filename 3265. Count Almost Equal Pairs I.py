class Solution:
    def valid(self, a: int, b: int) -> bool:
        if a==b:
            return True
        list1 = [0] * 10
        list2 = [0] * 10
        cnt = 0
        while a or b:
            temp1 = a % 10
            temp2 = b % 10
            a //= 10
            b //= 10
            if temp1 != temp2:
                cnt += 1
                if cnt > 2:
                    return False
            list1[temp1] += 1
            list2[temp2] += 1
        for i in range(10):
            if list1[i] != list2[i]:
                return False
        return True if cnt == 2 else False
    
    def countPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if self.valid(nums[i], nums[j]):
                    ans += 1
        return ans
