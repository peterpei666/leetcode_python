from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        while head:
            if not head.val == val:
                temp.next = head
                temp = head
            head = head.next
        temp.next = None
        return dummy.next
