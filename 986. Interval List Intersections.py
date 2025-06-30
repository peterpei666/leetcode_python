class Solution:
    def intervalIntersection(self, list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
        m, n = len(list1), len(list2)
        i, j = 0, 0
        ret = []
        while i < m and j < n:
            l = max(list1[i][0], list2[j][0])
            r = min(list1[i][1], list2[j][1])
            if l <= r:
                ret.append([l, r])
            if list1[i][1] < list2[j][1]:
                i += 1
            else:
                j += 1
        return ret
