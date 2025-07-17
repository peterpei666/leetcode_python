class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def valid(x: int) -> bool:
            pro = 1
            while x:
                pro *= x % 10
                x //= 10
            return True if pro % t == 0 else False
        
        while valid(n) == False:
            n += 1
        return n
