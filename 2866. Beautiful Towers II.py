class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        prefix = [0] * n
        stack = [-1]
        total = 0
        for i in range(n):
            while len(stack) > 1 and maxHeights[stack[-1]] > maxHeights[i]:
                j = stack.pop()
                total -= maxHeights[j] * (j - stack[-1])
            total += maxHeights[i] * (i - stack[-1])
            stack.append(i)
            prefix[i] = total
        suffix = [0] * n
        stack = [n]
        total = 0
        for i in range(n - 1, -1, -1):
            while len(stack) > 1 and maxHeights[stack[-1]] > maxHeights[i]:
                j = stack.pop()
                total -= maxHeights[j] * (stack[-1] - j)
            total += maxHeights[i] * (stack[-1] - i)
            stack.append(i)
            suffix[i] = total
        ans = 0
        for i in range(n):
            ans = max(ans, prefix[i] + suffix[i] - maxHeights[i])
        return ans
