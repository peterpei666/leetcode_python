class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = [0] * len(arr)
        lens = [0] * len(arr)
        for i, s in enumerate(arr):
            mask = 0
            for c in s:
                if mask & (1 << (ord(c) - ord('a'))):
                    mask = 0
                    break
                mask |= 1 << (ord(c) - ord('a'))
            masks[i] = mask
            lens[i] = len(s) if mask else 0
        def dfs(index, mask):
            if index == len(arr):
                return 0
            max_length = dfs(index + 1, mask)
            if masks[index] & mask == 0:
                max_length = max(max_length, lens[index] + dfs(index + 1, mask | masks[index]))
            return max_length
        return dfs(0, 0)
