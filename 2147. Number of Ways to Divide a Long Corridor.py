class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ans = 1
        valid = False
        mod = 10 ** 9 + 7
        cnt, temp = 0, 0
        for c in corridor:
            if c == 'S':
                if cnt == 2:
                    ans = ans * temp % mod
                    temp, cnt = 0, 0
                elif cnt == 1:
                    temp, valid = 1, True
                cnt += 1
            else:
                if cnt == 2:
                    temp += 1
        return 0 if cnt == 1 or not valid else ans % mod
