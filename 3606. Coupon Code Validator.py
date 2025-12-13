from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def check(s: str) -> bool:
            for c in s:
                if not c.isdigit() and not c.isalpha() and not c == '_':
                    return False
            return True
        
        ans = []
        n = len(code)
        t = ['electronics', 'grocery', 'pharmacy', 'restaurant']
        for k in t:
            temp = []
            for i in range(n):
                if businessLine[i] == k and isActive[i] and code[i] and check(code[i]):
                    temp.append(code[i])
            temp.sort()
            ans += temp
        return ans
