from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []
        stk = []
        cur = root
        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk[-1]
            stk.pop()
            inorder.append(cur)
            cur = cur.right
        stk = []
        pid = []
        stk.append(len(inorder) - 1)
        pid.append(-1)
        root_idx = 0
        while stk:
            val = stk[-1]
            l = val // 10001
            r = val % 10001
            p = pid[-1]
            stk.pop()
            pid.pop()
            mid = (l + r) // 2
            inorder[mid].left = None
            inorder[mid].right = None
            if p == -1:
                root_idx = mid
            elif mid < p:
                inorder[p].left = inorder[mid]
            else:
                inorder[p].right = inorder[mid]
            if r >= mid + 1:
                stk.append((mid + 1) * 10001 + r)
                pid.append(mid)
            if l <= mid - 1:
                stk.append(l * 10001 + mid - 1)
                pid.append(mid)
        return inorder[root_idx]
