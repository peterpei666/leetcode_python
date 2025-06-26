class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        temp = []
        for i in range(len(grid)):
            temp += sorted(grid[i], reverse=True)[:limits[i]]
        return sum(sorted(temp, reverse=True)[:k])
