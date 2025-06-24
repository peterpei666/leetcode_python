class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ret = list1
        for i in range(1, a):
            list1 = list1.next
        temp = list1.next
        for i in range(a, b + 1):
            temp = temp.next
        list1.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = temp
        return ret
