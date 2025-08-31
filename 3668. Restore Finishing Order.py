from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ord = [0] * 101
        n = len(order)
        for i in range(n):
            ord[order[i]] = i
        friends.sort(key=lambda x: ord[x])
        return friends
