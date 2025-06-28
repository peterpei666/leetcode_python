class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        def can_merge(a: List[int], b: List[int]) -> bool:
            if a[0] > b[1] or b[0] > a[1]:
                return False
            return True
        
        def merge(a: List[int], b: List[int]) -> List[int]:
            return [min(a[0], b[0]), max(a[1], b[1])]
        
        ranges.sort()
        n = len(ranges)
        i, cnt = 0, 0
        while i < n:
            temp = ranges[i]
            i += 1
            while i < n and can_merge(temp, ranges[i]):
                temp = merge(temp, ranges[i])
                i += 1
            cnt += 1
        return pow(2, cnt, 10 ** 9 + 7)
