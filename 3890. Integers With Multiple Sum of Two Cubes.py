from typing import List, DefaultDict
from bisect import bisect_right

mp = DefaultDict(int)
for i in range(1, 1001):
    for j in range(i, 1001):
        mp[i ** 3 + j ** 3] += 1
arr = sorted([x for x, n in mp.items() if n >= 2])

class Solution:
    def findGoodIntegers(self, n: int) -> List[int]:
        return arr[:bisect_right(arr, n)]
