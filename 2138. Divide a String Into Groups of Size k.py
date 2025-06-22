class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            temp = ''
            while i < len(s) and len(temp) < k:
                temp += s[i]
                i += 1
            while len(temp) < k:
                temp += fill
            ret.append(temp)
        return ret
