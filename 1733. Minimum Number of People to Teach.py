from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        mp = dict()
        m = len(languages)
        for i in range(1, m + 1):
            mp[i] = set(languages[i - 1])
        k = len(friendships)
        ans = m
        valid = set()
        for i in range(k):
            for lan in languages[friendships[i][0] - 1]:
                if lan in mp[friendships[i][1]]:
                    valid.add(i)
                    break
        for i in range(1, n + 1):
            taught = set()
            for j in range(k):
                if j in valid:
                    continue
                if not i in mp[friendships[j][0]]:
                    taught.add(friendships[j][0])
                if not i in mp[friendships[j][1]]:
                    taught.add(friendships[j][1])
            ans = min(ans, len(taught))
        return ans
