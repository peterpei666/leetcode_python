class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stk = []
        for i in arr:
            if stk and stk[-1] > i:
                temp = stk[-1]
                while stk and stk[-1] > i:
                    stk.pop()
                stk.append(temp)
            else:
                stk.append(i)
        return len(stk)
