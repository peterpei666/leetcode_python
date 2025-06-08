class Solution:
    def clearStars(self, s: str) -> str:
        lists=[[] for _ in range(26)]
        arr=list(s)
        for i,c in enumerate(arr):
            if c != '*':
                lists[ord(c)-ord('a')].append(i)
            else:
                for j in range(26):
                    if lists[j]:
                        arr[lists[j].pop()] = '*'
                        break
        return ''.join(c for c in arr if c != '*')

