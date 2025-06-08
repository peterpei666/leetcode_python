class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret=[]
        cur=1
        for _ in range(n):
            ret.append(cur)
            if cur*10 <=n:
                cur *=10
            else:
                while cur % 10 == 9 or cur >= n:
                    cur //= 10
                cur += 1
        return ret
