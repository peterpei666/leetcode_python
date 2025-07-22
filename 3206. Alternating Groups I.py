class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        cnt = 0
        for i in range(n):
            if colors[(i - 2 + n) % n] != colors[(i - 1 + n) % n] and colors[i] != colors[(i - 1 + n) % n]:
                cnt += 1
        return cnt
