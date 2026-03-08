from typing import List
from collections import defaultdict

class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.arr = [-1] * 26
        self.cnt = defaultdict(int)
        self.mp = values
        for i in range(len(keys)):
            self.arr[ord(keys[i]) - ord('a')] = i
        for s in dictionary:
            self.cnt[self.encrypt(s)] += 1

    def encrypt(self, word1: str) -> str:
        ans = ''
        for c in word1:
            if self.arr[ord(c) - ord('a')] == -1:
                return ''
            ans += self.mp[self.arr[ord(c) - ord('a')]]
        return ans

    def decrypt(self, word2: str) -> int:
       return self.cnt[word2]
