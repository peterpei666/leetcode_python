class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def is_inside(point, query):
            x, y = point
            x1, y1, r = query
            return (x - x1) ** 2 + (y - y1) ** 2 <= r ** 2

        result = [sum(1 for point in points if is_inside(point, query)) for query in queries]
        return result
