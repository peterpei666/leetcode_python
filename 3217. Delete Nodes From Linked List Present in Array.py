from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        mp = set(nums)
        ans = ListNode()
        t = ans
        while head:
            if not head.val in mp:
                t.next = head
                t = t.next
            head = head.next
        t.next = None
        return ans.next
