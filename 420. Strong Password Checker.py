class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        miss = 3
        if any(c.islower() for c in password):
            miss -= 1
        if any(c.isupper() for c in password):
            miss -= 1
        if any(c.isdigit() for c in password):
            miss -= 1
        n = len(password)
        change = 0
        one, two = 0, 0
        p = 2
        while p < n:
            if password[p] == password[p - 1] == password[p - 2]:
                l = 2
                while p < n and password[p] == password[p - 1] == password[p - 2]:
                    l += 1
                    p += 1
                change += l // 3
                if l % 3 == 0:
                    one += 1
                elif l % 3 == 1:
                    two += 1
            else:
                p += 1
        if n < 6:
            return max(miss, 6 - n)
        if n <= 20:
            return max(miss, change)
        delete = n - 20
        change -= min(delete, one)
        change -= min(max(delete - one, 0), two * 2) // 2
        change -= max(delete - one - 2 * two, 0) // 3
        return delete + max(miss, change)
