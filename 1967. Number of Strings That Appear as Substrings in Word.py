from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 if word.count(p) else 0 for p in patterns)
