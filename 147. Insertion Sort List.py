from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()
        cur = head
        dummy.next = head
        while cur and cur.next:
            if cur.next.val >= cur.val:
                cur = cur.next
            else:
                temp = cur.next
                cur.next = temp.next
                pre = dummy
                while pre.next.val <= temp.val:
                    pre = pre.next
                temp.next = pre.next
                pre,next = temp
        return dummy.next
