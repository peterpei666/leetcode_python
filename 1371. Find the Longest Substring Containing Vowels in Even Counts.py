class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        state = 0
        first_occurrence = {0: -1}
        max_length = 0
        for i, char in enumerate(s):
            if char in vowels:
                state ^= (1 << vowels[char])
            if state in first_occurrence:
                max_length = max(max_length, i - first_occurrence[state])
            else:
                first_occurrence[state] = i
        return max_length
