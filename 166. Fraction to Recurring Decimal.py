class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n % d == 0:
            return str(n // d)
        sign_n = n // abs(n)
        sign_d = d // abs(d)
        n = abs(n)
        d = abs(d)
        mp = dict()
        remain = n % d
        mp[remain] = 0
        temp = ""
        i = 1
        while remain:
            remain *= 10
            temp += str(remain // d)
            remain %= d
            if remain in mp:
                break
            mp[remain] = i
            i += 1
        if remain == 0:
            ans = str(n // d) + "." + temp
            if sign_d ^ sign_n:
                ans = "-" + ans
            return ans
        ans = str(n // d) + "." + temp[:mp[remain]] + "(" + temp[mp[remain]:] + ")"
        if sign_d ^ sign_n:
                ans = "-" + ans
        return ans
