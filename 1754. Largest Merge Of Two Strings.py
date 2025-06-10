class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ret = ""
        while word1 and word2:
            if word1 > word2:
                ret += word1[0]
                word1 = word1[1:]
            else:
                ret += word2[0]
                word2 = word2[1:]
        if word1:
            ret += word1
        if word2:
            ret += word2
        return ret
