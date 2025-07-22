class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        if currentEnergy < enemyEnergies[0]:
            return 0
        n = len(enemyEnergies) - 1
        ans = 0
        while n >= 0:
            if currentEnergy >= enemyEnergies[0]:
                ans += currentEnergy // enemyEnergies[0]
                currentEnergy %= enemyEnergies[0]
            else:
                currentEnergy += enemyEnergies[n]
                n -= 1
        return ans
