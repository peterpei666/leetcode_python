class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next or not head.next.next:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        stk = None
        while temp:
            t = temp.next
            temp.next = stk
            stk = temp
            temp = t
        temp = head
        while stk:
            t = temp.next
            temp.next = stk
            stk = stk.next
            temp.next.next = t
            temp = t
