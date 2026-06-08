from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        t1, t2 = [], []
        cnt = 0
        for i in nums:
            if i < pivot:
                t1.append(i)
            elif i > pivot:
                t2.append(i)
            else:
                cnt += 1
        return t1 + [pivot] * cnt + t2
