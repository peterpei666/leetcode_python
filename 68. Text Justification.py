from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n, i = len(words), 0
        ans = []
        while i < n:
            j = i
            cur, chrs = 0, 0
            while j < n and cur + len(words[j]) + j - i <= maxWidth:
                cur += len(words[j])
                chrs += len(words[j])
                j += 1
            line = ""
            space = maxWidth - chrs
            gap = j - i - 1
            if j == n or gap == 0:
                for k in range(i, j):
                    line += words[k]
                    if k != j - 1:
                        line += " "
                while len(line) < maxWidth:
                    line += " "
            else:
                each, extra = space // gap, space % gap
                for k in range(i, j):
                    line += words[k]
                    if k != j - 1:
                        if extra > 0:
                            line += " " * (each + 1)
                        else:
                            line += " " * each
                        extra -= 1
            ans.append(line)
            i = j
        return ans
