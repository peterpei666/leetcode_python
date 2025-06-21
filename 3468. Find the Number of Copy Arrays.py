class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        m1 = bounds[0][0]
        m2 = bounds[0][1]
        for i in range(1, len(original)):
            m1 = m1 + original[i] - original[i - 1]
            m2 = m2 + original[i] - original[i - 1]
            m1 = max(m1, bounds[i][0])
            m2 = min(m2, bounds[i][1])
            if m1 > m2:
                return 0
        return m2 - m1 + 1
