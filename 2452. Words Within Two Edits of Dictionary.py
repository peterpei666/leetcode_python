class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        dictionary.sort()
        ret = []
        for s in queries:
            sz = len(s)
            for w in dictionary:
                temp = len(w)
                if temp < sz:
                    continue
                if temp > sz:
                    break
                cnt = 0
                for i in range(sz):
                    if s[i] != w[i]:
                        cnt += 1
                        if cnt > 2:
                            break
                if cnt <= 2:
                    ret.append(s)
                    break
        return ret
