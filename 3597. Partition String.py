class Solution:
    def partitionString(self, s: str) -> List[str]:
        mp = dict()
        temp = ""
        for c in s:
            temp += c
            if not temp in mp:
                mp[temp] = True
                temp = ""
        ret = []
        for key in mp:
            ret.append(key)
        return ret
