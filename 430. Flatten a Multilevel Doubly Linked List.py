class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Node) -> Node:
        if not head:
            return head
        stk = []
        dummy = Node(0, None, None, None)
        tail = dummy
        temp = head
        while temp or stk:
            if not temp:
                temp = stk.pop()
            temp.prev = tail
            tail.child = None
            tail.next = temp
            tail = temp
            if temp.child:
                if temp.next:
                    stk.append(temp.next)
                temp = temp.child
            else:
                temp = temp.next
        tail.next = None
        tail.child = None
        if dummy.next:
            dummy.next.prev = None
        return dummy.next
