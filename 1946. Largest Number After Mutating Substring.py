class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)
        i = 0
        n = len(num)
        while i < n and change[int(num[i])] <= int(num[i]):
            i += 1
        while i < n and change[int(num[i])] >= int(num[i]):
            num[i] = str(change[int(num[i])])
            i += 1
        return "".join(num)
