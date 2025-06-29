class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def lcp(a: str, b: str) -> int:
            i, n = 0, min(len(a), len(b))
            while i < n and a[i] == b[i]:
                i += 1
            return i
        
        n = len(words)
        if n == 1:
            return [0]
        cnt = [0] * (n - 1)
        for i in range(n - 1):
            cnt[i] = lcp(words[i], words[i + 1])
        prefix = [0] * (n - 1)
        prefix[0] = cnt[0]
        for i in range(1, n - 1):
            prefix[i] = max(prefix[i - 1], cnt[i])
        suffix = [0] * (n - 1)
        suffix[-1] = cnt[-1]
        for i in range(n - 3, -1, -1):
            suffix[i] = max(suffix[i + 1], cnt[i])
        ret = [0] * n
        for i in range(n):
            temp = 0
            if i > 0 and i < n - 1:
                temp = max(temp, lcp(words[i-1], words[i+1]))
            if i - 2 >= 0:
                temp=max(temp, prefix[i - 2])
            if i + 1 < n - 1:
                temp=max(temp, suffix[i + 1])
            ret[i] = temp
        return ret
