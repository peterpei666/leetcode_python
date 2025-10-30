class Solution:
    def simplifyPath(self, path: str) -> str:
        words = path.split('/')
        ans = []
        for w in words:
            if w == '..':
                if ans:
                    ans.pop()
                continue
            if w == '' or w == '.':
                continue
            ans.append('/' + w)
        return ''.join(ans) if ans else '/'
