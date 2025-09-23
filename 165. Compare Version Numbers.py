class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n = len(version1), len(version2)
        i, j = 0, 0
        while i < m or j < n:
            temp1 = 0
            while i < m and not version1[i] == '.':
                temp1 = temp1 * 10 - ord('0') + ord(version1[i])
                i += 1
            i += 1
            temp2 = 0
            while j < n and not version2[j] == '.':
                temp2 = temp2 * 10 - ord('0') + ord(version2[j])
                j += 1
            j += 1
            if temp1 > temp2:
                return 1
            if temp1 < temp2:
                return -1
        return 0
