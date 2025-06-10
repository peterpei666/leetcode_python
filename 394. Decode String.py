class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""
        for c in s:
            if c.isdigit():
                current_num = current_num * 10 + int(c)
            elif c == '[':
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif c == ']':
                last_str, count = stack.pop()
                current_str = last_str + current_str * count
            else:
                current_str += c
        return current_str
