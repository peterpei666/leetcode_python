class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        prefix = [0] * n
        prefix[0] = 1
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = 1
        suffix = [0] * n
        suffix[n - 1] = 1
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                suffix[i] = suffix[i + 1] + 1
            else:
                suffix[i] = 1
        ret = []
        for i in range(n):
            if prefix[i] > time and suffix[i] > time:
                ret.append(i)
        return ret
