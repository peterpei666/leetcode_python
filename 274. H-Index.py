from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        ans = citations[0]
        i = 0
        while ans > i:
            while i < n and citations[i] >= ans:
                i += 1
            if ans <= i:
                break
            ans -= 1
        return ans
