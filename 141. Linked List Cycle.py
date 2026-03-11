class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast, slow = head, head
        while 1:
            if not fast.next or not fast.next.next:
                return False
            fast = fast.next.next
            if fast == slow:
                return True
            slow = slow.next
