from typing import List

class Solution:
    def toggleLightBulbs(self, bulbs: List[int]) -> List[int]:
        mp = [0] * 101
        for i in bulbs:
            mp[i] ^= 1
        return [i for i, n in enumerate(mp) if n]
