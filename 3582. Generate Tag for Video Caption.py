class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words:
            return '#'
        ret = '#' + words[0].lower()
        for word in words[1:]:
            ret += word.capitalize()
        return ret[:100]
