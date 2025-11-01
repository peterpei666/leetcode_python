from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        ans = ListNode()
        pre, cur, temp = dummy, head, ans
        while cur:
            if cur.val < x:
                pre.next = cur.next
                temp.next = cur
                temp = cur
            else:
                pre = cur
            cur = cur.next
        temp.next = dummy.next
        return ans.next
