class Solution:
    def reverseByType(self, s: str) -> str:
        letter = []
        special = []
        for char in s:
            if char.isalpha():
                letter.append(char)
            else:
                special.append(char)
        letter.reverse()
        special.reverse()
        result = []
        letter_idx = 0
        special_idx = 0
        for char in s:
            if char.isalpha():
                result.append(letter[letter_idx])
                letter_idx += 1
            else:
                result.append(special[special_idx])
                special_idx += 1
        return ''.join(result)
