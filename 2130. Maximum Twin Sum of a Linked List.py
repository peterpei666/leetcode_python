class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode) -> int:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev = prev, slow.next
            slow, prev = prev, slow
        ans = 0
        while slow:
            ans = max(ans, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return ans
