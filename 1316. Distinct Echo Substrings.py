class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        mp = set()
        n = len(text)
        for i in range(1, n - 1):
            j = 1
            while i >= j and i + j - 1 < n:
                if text[i-j:i] == text[i:i+j]:
                    mp.add(text[i:i+j])
                j += 1
        return len(mp)
