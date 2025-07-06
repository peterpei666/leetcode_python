from collections import defaultdict

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.arr1 = nums1
        self.arr2 = nums2
        self.mp = defaultdict(int)
        for num in nums2:
            self.mp[num] += 1

    def add(self, index: int, val: int) -> None:
        self.mp[self.arr2[index]] -= 1
        if self.mp[self.arr2[index]] == 0:
            del self.mp[self.arr2[index]]
        self.arr2[index] += val
        self.mp[self.arr2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.mp[tot - num] for num in self.arr1 if tot - num in self.mp)
