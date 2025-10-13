from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        cur = [0] * 26
        pre = [0] * 26
        ans = [words[0]]
        for c in words[0]:
            pre[ord(c) - ord('a')] += 1
        for w in words[1:]:
            for c in w:
                cur[ord(c) - ord('a')] += 1
            if not pre == cur:
                ans.append(w)
                pre = cur[:]
            cur = [0] * 26
        return ans
