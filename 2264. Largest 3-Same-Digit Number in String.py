class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = ""
        for i in range(n - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if len(ans) == 0 or ord(ans[0]) < ord(num[i]):
                    ans = num[i] * 3
        return ans
