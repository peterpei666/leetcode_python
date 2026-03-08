from typing import List

class Solution:
    class TrieNode:
        def __init__(self):
            self.child = dict()
            self.cnt = 0

    def add(self, s: str) -> None:
        temp = self.root
        for c in s:
            if not ord(c) - ord('a') in temp.child:
                temp.child[ord(c) - ord('a')] = self.TrieNode()
            temp = temp.child[ord(c) - ord('a')]
            temp.cnt += 1

    def get(self, s: str) -> int:
        ans = 0
        temp = self.root
        for c in s:
            if not ord(c) - ord('a') in temp.child:
                break
            temp = temp.child[ord(c) - ord('a')]
            ans += temp.cnt
        return ans
    
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.root = self.TrieNode()
        for s in words:
            self.add(s)
        return [self.get(s) for s in words]
