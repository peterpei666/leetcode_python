class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        cur = [0] * 4
        temp = [0] * 4
        ans = 0
        for ch in s:
            nxt = cur[:]
            tmp = temp[:]
            if ch == 'N':
                nxt[0] += 1
                nxt[1] += 1
                if tmp[2] < k:
                    nxt[2] += 1
                    tmp[2] += 1
                else:
                    nxt[2] -= 1
                if tmp[3] < k:
                    nxt[3] += 1
                    tmp[3] += 1
                else:
                    nxt[3] -= 1
            elif ch == 'S':
                nxt[2] += 1
                nxt[3] += 1
                if tmp[0] < k:
                    nxt[0] += 1
                    tmp[0] += 1
                else:
                    nxt[0] -= 1
                if tmp[1] < k:
                    nxt[1] += 1
                    tmp[1] += 1
                else:
                    nxt[1] -= 1
            elif ch == 'W':
                nxt[1] += 1
                nxt[3] += 1
                if tmp[0] < k:
                    nxt[0] += 1
                    tmp[0] += 1
                else:
                    nxt[0] -= 1
                if tmp[2] < k:
                    nxt[2] += 1
                    tmp[2] += 1
                else:
                    nxt[2] -= 1
            elif ch == 'E':
                nxt[0] += 1
                nxt[2] += 1
                if tmp[1] < k:
                    nxt[1] += 1
                    tmp[1] += 1
                else:
                    nxt[1] -= 1
                if tmp[3] < k:
                    nxt[3] += 1
                    tmp[3] += 1
                else:
                    nxt[3] -= 1
            cur, temp = nxt, tmp
            ans = max(ans, max(cur))
        return ans
