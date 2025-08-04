from typing import List
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        mp = set(wordList)
        if endWord not in mp:
            return 0
        begin = {beginWord}
        end = {endWord}
        visited = set()
        step = 1
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
            next = set()
            for word in begin:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c == word[i]:
                            continue
                        temp = word[:i] + c + word[i + 1:]
                        if temp in end:
                            return step + 1
                        if temp in mp and temp not in visited:
                            next.add(temp)
                            visited.add(temp)
            begin = next
            step += 1
        return 0
