class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seq = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        def dfs(index: int) -> bool:
            if index == len(seq):
                return True
            if seq[index] != 0:
                return dfs(index + 1)
            for i in range(n, 0, -1):
                if not used[i]:
                    if i == 1 or (index + i < len(seq) and seq[index + i] == 0):
                        seq[index] = i
                        used[i] = True
                        if i > 1:
                            seq[index + i] = i
                        if dfs(index + 1):
                            return True
                        seq[index] = 0
                        used[i] = False
                        if i > 1:
                            seq[index + i] = 0
            return False
        dfs(0)
        return seq
