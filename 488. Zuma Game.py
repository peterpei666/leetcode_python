from collections import deque

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        def update(s: str, idx: int) -> str:
            if idx < 0:
                return s
            l, r = idx, idx
            while l > 0 and s[l] == s[l - 1]:
                l -= 1
            while r < len(s) - 1 and s[r] == s[r + 1]:
                r += 1
            if r - l + 1 >= 3:
                return update(s[:l] + s[r + 1:], l - 1)
            return s
        
        hand = list(hand)
        hand.sort()
        hand = "".join(hand)
        bq = deque()
        hq = deque()
        stepq = deque()
        mp = set()
        bq.append(board)
        hq.append(hand)
        stepq.append(0)
        mp.add(board + '/' + hand)
        while stepq:
            curb = bq[0]
            curh = hq[0]
            cur = stepq[0]
            bq.popleft()
            hq.popleft()
            stepq.popleft()
            for i in range(len(curb)):
                for j in range(len(curh)):
                    if j > 0 and curh[j] == curh[j - 1]:
                        continue
                    if i > 0 and curb[i - 1] == curh[j]:
                        continue
                    worth = False
                    if curb[i] == curh[j]:
                        worth = True
                    elif i > 0 and curb[i] == curb[i - 1] and not curb[i] == curh[j]:
                        worth = True
                    if worth:
                        newb = update(curb[:i] + curh[j] + curb[i:], i)
                        if newb == "":
                            return cur + 1
                        newh = curh[:j] + curh[j + 1:]
                        if newb + "/" + newh not in mp:
                            bq.append(newb)
                            hq.append(newh)
                            stepq.append(cur + 1)
                            mp.add(newb + "/" + newh)
        return -1
