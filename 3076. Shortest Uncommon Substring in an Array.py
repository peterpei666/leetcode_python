from typing import List

class Solution:
    class TrieNode:
        def __init__(self):
            self.child = dict()
            self.cnt = 0

    def add(self, s: str, i: int, j: int) -> None:
        temp = self.root
        for k in range(i, j):
            if not ord(s[k]) - ord('a') in temp.child:
                temp.child[ord(s[k]) - ord('a')] = self.TrieNode()
            temp = temp.child[ord(s[k]) - ord('a')]
            temp.cnt += 1

    def get(self, s: str, i: int, j: int) -> bool:
        temp = self.root
        for k in range(i, j):
            if temp.child[ord(s[k]) - ord('a')].cnt == 0:
                return True
            temp = temp.child[ord(s[k]) - ord('a')]
        return False
    
    def remove(self, s: str, i: int, j: int) -> None:
        temp = self.root
        for k in range(i, j):
            temp = temp.child[ord(s[k]) - ord('a')]
            temp.cnt -= 1
    
    def shortestSubstrings(self, arr: List[str]) -> List[int]:
        self.root = self.TrieNode()
        for s in arr:
            n = len(s)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    self.add(s, i, j)
        ans = []
        for s in arr:
            n = len(s)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    self.remove(s, i, j)
            ret = 'zzzzzzzzzzzzzzzzzzzzzzzzz'
            for i in range(n):
                for j in range(i + 1, n + 1):
                    if self.get(s, i, j):
                        if j - i < len(ret) or (j - i <= len(ret) and s[i:j] < ret):
                            ret = s[i:j]
            for i in range(n):
                for j in range(i + 1, n + 1):
                    self.add(s, i, j)
            ans.append('' if ret == 'zzzzzzzzzzzzzzzzzzzzzzzzz' else ret)
        return ans
