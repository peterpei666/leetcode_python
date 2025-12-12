from typing import List

class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), x[0] == 'MESSAGE'))
        cnt = [0] * n
        next = [0] * n
        for e in events:
            cur = int(e[1])
            if e[0] == 'MESSAGE':
                if e[2] == 'ALL':
                    for i in range(n):
                        cnt[i] += 1
                elif e[2] == 'HERE':
                    for i, t in enumerate(next):
                        if t <= cur:
                            cnt[i] += 1
                else:
                    for idx in e[2].split():
                        cnt[int(idx[2:])] += 1
            else:
                next[int(e[2])] = cur + 60
        return cnt
