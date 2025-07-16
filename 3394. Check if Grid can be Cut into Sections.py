class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        n = len(rectangles)
        def check(d: int) -> bool:
            rectangles.sort(key=lambda x: x[d])
            cnt = 0
            cur = rectangles[0][d + 2]
            for i in range(1, n):
                if cur <= rectangles[i][d]:
                    cnt += 1
                    if cnt >= 2:
                        return True
                cur = max(cur, rectangles[i][d + 2])
            return False
        
        return check(0) or check(1)
