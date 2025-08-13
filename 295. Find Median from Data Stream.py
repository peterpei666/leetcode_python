from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxheap, -num)
        heappush(self.minheap, -heappop(self.maxheap))
        if len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.minheap) < len(self.maxheap):
            return -self.maxheap[0]
        return (-self.maxheap[0] + self.minheap[0]) / 2
