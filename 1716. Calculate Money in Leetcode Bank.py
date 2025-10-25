class Solution:
    def totalMoney(self, n: int) -> int:
        temp = [0] * 7
        ans = 0
        for i in range(n):
            if i % 7 == 0:
                temp[0] += 1
                ans += temp[0]
            else:
                temp[i % 7] = temp[(i - 1) % 7] + 1
                ans += temp[i % 7]
        return ans
