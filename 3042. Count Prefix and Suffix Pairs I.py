from typing import List

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.cnt = 0
        
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = self.TrieNode()
        ans = 0
        for s in words:
            n = len(s)
            node = root
            for i in range(n):
                mask = ord(s[i]) * 128 + ord(s[n - i - 1])
                if not mask in node.children:
                    node.children[mask] = self.TrieNode()
                node = node.children[mask]
                ans += node.cnt
            node.cnt += 1
        return ans
