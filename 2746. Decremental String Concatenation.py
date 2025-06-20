class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        dp = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            dp[i][i] = 0
        for word in words:
            first_char = ord(word[0]) - ord('a')
            last_char = ord(word[-1]) - ord('a')
            new_dp = [[float('inf')] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    if dp[i][j] < float('inf'):
                        new_dp[i][last_char] = min(new_dp[i][last_char], dp[i][j] + len(word) - (1 if j == first_char else 0))
                        new_dp[first_char][j] = min(new_dp[first_char][j], dp[i][j] + len(word) - (1 if i == last_char else 0))
            dp = new_dp
        return min(dp[i][j] for i in range(26) for j in range(26))
