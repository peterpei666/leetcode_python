class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total_happiness = 0
        for i in range(min(len(happiness), k)):
            if happiness[i] < i:
                break
            total_happiness += happiness[i] - i
        return total_happiness
