from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def maxsub(nums: List[int], k: int) -> List[int]:
            stk = []
            drop = len(nums) - k
            for i in nums:
                while drop and stk and stk[-1] < i:
                    stk.pop()
                    drop -= 1
                stk.append(i)
            return stk[:k]
        
        def merge(seq1: List[int], seq2: List[int]) -> List[int]:
            m, n = len(seq1), len(seq2)
            i, j = 0, 0
            ans = []
            while i < m or j < n:
                if seq1[i:] > seq2[j:]:
                    ans.append(seq1[i])
                    i += 1
                else:
                    ans.append(seq2[j])
                    j += 1
            return ans
        
        m, n = len(nums1), len(nums2)
        ans = []
        for i in range(max(0, k - n), min(k, m) + 1):
            seq1 = maxsub(nums1, i)
            seq2 = maxsub(nums2, k - i)
            temp = merge(seq1, seq2)
            ans = max(ans, temp)
        return ans
