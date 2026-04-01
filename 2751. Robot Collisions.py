from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        mp = list(range(len(positions)))
        mp.sort(key=lambda x : positions[x])
        stk = []
        for idx in mp:
            hp = healths[idx]
            dir = directions[idx]
            if not stk or dir == 'R':
                stk.append((idx, hp, dir))
                continue
            while stk and stk[-1][2] == 'R':
                temp = stk[-1]
                stk.pop()
                if temp[1] == hp:
                    hp = 0
                    break
                elif temp[1] < hp:
                    hp -= 1
                else:
                    hp = 0
                    stk.append((temp[0], temp[1] - 1, temp[2]))
                    break
            if hp:
                stk.append((idx, hp, dir))
        stk.sort(key=lambda x : x[0])
        return [hp for _, hp, _ in stk]
