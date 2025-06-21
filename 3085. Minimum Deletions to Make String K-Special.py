class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        n = len(word)
        cnt = [0] * 26
        for c in word:
            cnt[ord(c) - ord('a')] += 1
        cnt.sort(reverse=True)
        for i in range(26):
            if cnt[i] == 0:
                break
            temp = 0
            for j in range(i):
                temp += max(0, cnt[j] - cnt[i] - k)
            for j in range(i + 1, 26):
                if cnt[j] == 0:
                    break
                temp += cnt[j]
            n = min(n, temp)
        return n
