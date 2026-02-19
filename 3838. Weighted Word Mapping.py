from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return ''.join(['abcdefghijklmnopqrstuvwxyz'[25 - sum(weights[ord(c) - ord('a')] for c in w) % 26] for w in words])
