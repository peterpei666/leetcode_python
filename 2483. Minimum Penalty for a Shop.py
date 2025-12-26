class Solution:
    def bestClosingTime(self, customers: str) -> int:
        temp = 0
        for c in customers:
            if c == 'Y':
                temp += 1
        ans = temp
        t = 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                temp -= 1
            else:
                temp += 1
            if ans > temp:
                ans = temp
                t = i + 1
        return t
