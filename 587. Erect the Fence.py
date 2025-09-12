from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort()

        def cmp(p1, p2, p3) -> int:
            return (p3[1] - p2[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p3[0] - p2[0])
        
        lower = []
        upper = []
        for p in trees:
            while len(lower) >= 2 and cmp(lower[-2], lower[-1], p) > 0:
                lower.pop()
            while len(upper) >= 2 and cmp(upper[-2], upper[-1], p) < 0:
                upper.pop()
            lower.append(tuple(p))
            upper.append(tuple(p))
        return list(set(lower + upper))
