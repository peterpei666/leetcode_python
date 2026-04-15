from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = 1000
        for i in range(n):
            if words[i] == target:
                ans = min(ans, min(abs(i - startIndex), n - abs(i - startIndex)));
        return -1 if ans == 1000 else ans
