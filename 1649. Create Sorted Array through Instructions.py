from typing import List

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        tree = [0] * 100005
        MAX = 100001

        def update(x: int) -> None:
            while x < MAX:
                tree[x] += 1
                x += x & -x
        
        def query(x: int) -> int:
            ans = 0
            while x > 0:
                ans += tree[x]
                x -= x & -x
            return ans
        
        n = len(instructions)
        ans = 0
        mod = 10 ** 9 + 7
        for i in range(n):
            left = query(instructions[i] - 1)
            right = i - query(instructions[i])
            ans += min(left, right)
            update(instructions[i])
        return ans % mod
