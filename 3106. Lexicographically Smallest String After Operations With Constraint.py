class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans = ""
        for i, num in enumerate(map(lambda x: ord(x) - 97, s)):
            dist = min(num, 26 - num)
            if dist <= k:
                k -= dist
                ans += 'a'
            else:
                ans += chr(num + 97 - k)
                break
        return ans + s[i+1:]
