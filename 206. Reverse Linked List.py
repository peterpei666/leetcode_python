from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = None
        while head:
            temp = head.next
            head.next = stk
            stk = head
            head = temp
        return stk
