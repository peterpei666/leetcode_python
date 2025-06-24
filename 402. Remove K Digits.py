class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ret = []
        for c in num:
            while k and ret and ret[-1] > c:
                ret.pop()
                k -= 1
            ret.append(c)
        ret = ret[:len(ret) - k]
        return ''.join(ret).lstrip('0') or '0'
