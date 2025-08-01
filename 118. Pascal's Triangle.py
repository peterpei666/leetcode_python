from typing import List

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = []
        for i in range(1, n + 1):
            temp = [0] * i
            temp[0]=1
            temp[i-1]=1
            for j in range(1, i - 1):
                temp[j]=ans[i-2][j-1]+ans[i-2][j]
            ans.append(temp)
        return ans
