class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def count(l: int, r: int) -> int:
            ans = 0
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            return ans
        
        return sum(count(i, i) + count(i, i + 1) for i in range(n))
