class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        mp = []
        op = ['a', 'b', 'c']

        def generate(s: str) -> None:
            if len(s) == n:
                mp.append(s)
                return
            for i in range(3):
                if not s or not s[-1] == op[i]:
                    generate(s + op[i])

        generate('')
        mp.sort()
        return mp[k - 1] if k <= len(mp) else ''
