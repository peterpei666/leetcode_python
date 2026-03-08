from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        total = sum(len(s) for s in words)
        trie = [[0] * 26 for _ in range(total + 1)]
        count = [0] * (total + 1)
        depth = [0] * (total + 1)
        dep_cnt = [0] * 10001
        cur_max = 0
        cnt = 1

        def update(t: int, k: int, d: int) -> None:
            nonlocal cur_max
            old = count[t]
            count[t] += d
            dep = depth[t]
            if old < k and count[t] >= k:
                if dep_cnt[dep] == 0:
                    cur_max = max(cur_max, dep)
                dep_cnt[dep] += 1
            elif old >= k and count[t] < k:
                dep_cnt[dep] -= 1
                while cur_max > 0 and dep_cnt[cur_max] == 0:
                    cur_max -= 1

        def change(s: str, k: int, d: int) -> None:
            nonlocal cnt
            cur = 0
            for c in s:
                idx = ord(c) - ord('a')
                if trie[cur][idx] == 0:
                    depth[cnt] = depth[cur] + 1
                    trie[cur][idx] = cnt
                    cnt += 1
                cur = trie[cur][idx]
                update(cur, k, d)

        n = len(words)
        for i in range(n):
            change(words[i], k, 1)
        ans = [0] * n
        for i in range(n):
            change(words[i], k, -1)
            ans[i] = cur_max
            change(words[i], k, 1)
        return ans
