class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def mergeSort(head: ListNode, sz: int) -> ListNode:
            if sz == 1:
                return head
            mid = sz // 2
            t = head
            for _ in range(mid - 1):
                t = t.next
            t2 = mergeSort(t.next, sz - mid)
            t.next = None
            t1 = mergeSort(head, mid)
            dummy = ListNode()
            temp = dummy
            while t1 and t2:
                if t1.val < t2.val:
                    temp.next = t1
                    temp = t1
                    t1 = t1.next
                else:
                    temp.next = t2
                    temp = t2
                    t2 = t2.next
            temp.next = t1 if t1 else t2
            return dummy.next
        
        sz = 0
        temp = head
        while temp:
            sz += 1
            temp = temp.next
        return mergeSort(head, sz) if head else head
