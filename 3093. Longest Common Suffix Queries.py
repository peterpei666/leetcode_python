from typing import List

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        total = sum(len(s) for s in wordsContainer)
        trie = [[0] * 26 for _ in range(total + 1)]
        id = [0] * (total + 1)
        sz = [float('inf')] * (total + 1)
        cnt = 1

        def add(s: str, idx: int) -> None:
            nonlocal cnt
            cur = 0
            n = len(s)
            if n < sz[cur]:
                sz[cur] = n
                id[cur] = idx
            for i in range(n - 1, -1, -1):
                c = ord(s[i]) - ord('a')
                if trie[cur][c] == 0:
                    trie[cur][c] = cnt
                    cnt += 1
                cur = trie[cur][c]
                if n < sz[cur]:
                    sz[cur] = n
                    id[cur] = idx

        def query(s: str) -> int:
            cur = 0
            n = len(s)
            for i in range(n - 1, -1, -1):
                c = ord(s[i]) - ord('a')
                if trie[cur][c] == 0:
                    break
                cur = trie[cur][c]
            return id[cur]
        

        for i in range(len(wordsContainer)):
            add(wordsContainer[i], i)
        return [query(s) for s in wordsQuery]
