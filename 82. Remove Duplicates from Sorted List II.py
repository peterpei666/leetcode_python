from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        t = head
        while t:
            val = t.val
            node = t.next
            count = 1
            while node and node.val == val:
                count += 1
                node = node.next
            if count == 1:
                t.next = None
                tail.next = t
                tail = t
            t = node
        return dummy.next
