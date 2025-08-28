class node:
    def __init__(self, cnt: int):
        self.cnt = cnt
        self.prev = None
        self.next = None
        self.keys = set()

class AllOne:
    def __init__(self):
        self.head = node(0)
        self.tail = node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mp = dict()

    def remove(self, temp: node) -> None:
        temp.next.prev = temp.prev
        temp.prev.next = temp.next

    def inc(self, key: str) -> None:
        if key in self.mp:
            temp = self.mp[key]
            temp.keys.remove(key)
            if temp.next.cnt == temp.cnt + 1:
                temp.next.keys.add(key)
                self.mp[key] = temp.next
            else:
                newnode = node(temp.cnt + 1)
                newnode.keys.add(key)
                newnode.prev = temp
                newnode.next = temp.next
                temp.next.prev = newnode
                temp.next = newnode
                self.mp[key] = newnode
            if not temp.keys:
                self.remove(temp)
        else:
            if self.head.next.cnt == 1:
                self.head.next.keys.add(key)
                self.mp[key] = self.head.next
            else:
                newnode = node(1)
                newnode.keys.add(key)
                newnode.prev = self.head
                newnode.next = self.head.next
                self.head.next.prev = newnode
                self.head.next = newnode
                self.mp[key] = newnode

    def dec(self, key: str) -> None:
        temp = self.mp[key]
        temp.keys.remove(key)
        if temp.cnt == 1:
            del self.mp[key]
        elif temp.prev.cnt == temp.cnt - 1:
            temp.prev.keys.add(key)
            self.mp[key] = temp.prev
        else:
            newnode = node(temp.cnt - 1)
            newnode.keys.add(key)
            newnode.prev = temp.prev
            newnode.next = temp
            temp.prev.next = newnode
            temp.prev = newnode
            self.mp[key] = newnode
        if not temp.keys:
            self.remove(temp)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys)) 
