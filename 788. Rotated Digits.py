class Solution:
    def rotatedDigits(self, n: int) -> int:
        def valid(x: int) -> bool:
            ans = False
            while x:
                if x % 10 in [3, 4, 7]:
                    return False
                if x % 10 in [2, 5, 6, 9]:
                    ans = True
                x //= 10
            return ans
        
        return sum(1 for i in range(1, n + 1) if valid(i))
