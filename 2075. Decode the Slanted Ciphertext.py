class Solution:
    def decodeCiphertext(self, encodedText: str, m: int) -> str:
        n = len(encodedText) // m
        ans = ''
        for i in range(n):
            for k in range(min(m, n - i)):
                idx = i + k * n + k
                ans += encodedText[idx]
        return ans.rstrip()
