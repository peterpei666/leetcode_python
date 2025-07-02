class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(word)
        cnt = 1
        freq = []
        for i in range(1, n):
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                freq.append(cnt)
                cnt = 1
        freq.append(cnt)
        ans = 1
        for i in freq:
            ans = ans * i % mod
        if len(freq) >= k:
            return ans
        f = [0] * k
        g = [1] * k
        f[0] = 1
        m = len(freq)
        for i in range(m):
            nf = [0] * k
            for j in range(1, k):
                nf[j] = g[j - 1]
                if j - freq[i] - 1 >= 0:
                    nf[j] = (nf[j] - g[j - freq[i] - 1] + mod) % mod
            ng = [0] * k
            ng[0] = nf[0]
            for j in range(1, k):
                ng[j] = (ng[j - 1] + nf[j]) % mod
            f = nf
            g = ng
        return (ans - g[-1] + mod) % mod
