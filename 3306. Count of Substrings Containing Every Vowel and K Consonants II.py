class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        v = ['a', 'e', 'i', 'o', 'u']
        cnt = {c: 0 for c in v}

        def valid() -> bool:
            return all(cnt[i] > 0 for i in v)
        
        def vowel(c: chr) -> bool:
            return True if c in v else False
        
        n = len(word)
        next = [0] * n
        temp = n
        for i in range(n - 1, -1, -1):
            next[i] = temp
            if not vowel(word[i]):
                temp = i
        l = 0
        con = 0
        ans = 0
        for r in range(n):
            if vowel(word[r]):
                cnt[word[r]] += 1
            else:
                con += 1
            while con > k:
                if vowel(word[l]):
                    cnt[word[l]] -= 1
                else:
                    con -= 1
                l += 1
            while con == k and valid() and l < n:
                ans += next[r] - r
                if vowel(word[l]):
                    cnt[word[l]] -= 1
                else:
                    con -= 1
                l += 1
        return ans
