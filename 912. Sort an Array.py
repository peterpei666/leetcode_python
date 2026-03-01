from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(i: int, sz: int) -> None:
            largest = i
            while True:
                l = 2 * i + 1
                r = 2 * i + 2
                if l < sz and nums[l] > nums[largest]:
                    largest = l
                if r < sz and nums[r] > nums[largest]:
                    largest = r
                if i == largest:
                    break
                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest

        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            heapify(i, n)
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(0, i)
        return nums
