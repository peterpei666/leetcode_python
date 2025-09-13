class Solution:
    def isValid(self, code: str) -> bool:
        stk = []
        seen_tag = False

        def tagName(s: str, ending: bool) -> bool:
            nonlocal stk, seen_tag
            if len(s) < 1 or len(s) > 9:
                return False
            if not all('A' <= c <= 'Z' for c in s):
                return False
            if ending:
                if stk and stk[-1] == s:
                    stk.pop()
                else:
                    return False
            else:
                seen_tag = True
                stk.append(s)
            return True

        def isCDataStart(s: str) -> bool:
            return s.startswith('[CDATA[')

        if not code or code[0] != '<' or code[-1] != '>':
            return False
        i, n = 0, len(code)
        while i < n:
            if not stk and seen_tag:
                return False
            if code[i] != '<':
                if not stk:
                    return False
                i += 1
                continue
            if i + 1 >= n:
                return False
            if code[i + 1] == '!':
                if not stk:
                    return False
                close_idx = code.find(']]>', i + 1)
                if close_idx == -1:
                    return False
                if not isCDataStart(code[i + 2:close_idx]):
                    return False
                i = close_idx + 3
                continue
            ending = False
            if code[i + 1] == '/':
                ending = True
                i += 1
            close_idx = code.find('>', i + 1)
            if close_idx == -1:
                return False
            name = code[i + 1:close_idx]
            if not tagName(name, ending):
                return False
            i = close_idx + 1
        return not stk and seen_tag
