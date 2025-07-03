class Solution:
    def kthCharacter(self, k: int) -> str:
        cur = ['a']
        while len(cur) < k:
            temp = cur[:]
            for i in range(len(temp)):
                temp[i] = chr((ord(temp[i]) - ord('a') + 1) % 26 + ord('a'))
            cur += temp
        return cur[k - 1]
