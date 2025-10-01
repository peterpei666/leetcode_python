from typing import List

class node:
    def __init__(self):
        self.children = dict()
        self.idx = -1

class WordFilter:
    def __init__(self, words: List[str]):
        self.root = node()
        for index, word in enumerate(words):
            l = len(word)
            for i in range(l + 1):
                cur = self.root
                suf = word[i:] + '#' + word
                for c in suf:
                    if not c in cur.children:
                        cur.children[c] = node()
                    cur = cur.children[c]
                    cur.idx = index

    def f(self, pref: str, suff: str) -> int:
        word = suff + "#" + pref
        cur = self.root
        for c in word:
            if not c in cur.children:
                return -1
            cur = cur.children[c]
        return cur.idx
