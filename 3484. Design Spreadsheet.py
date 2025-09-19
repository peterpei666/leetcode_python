class Spreadsheet:
    def __init__(self, rows: int):
        self.mp = dict()

    def setCell(self, cell: str, value: int) -> None:
        self.mp[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.mp:
            del self.mp[cell]

    def getValue(self, formula: str) -> int:
        n = len(formula)
        if ord('A') <= ord(formula[1]) <= ord('Z'):
            key = ''
            i = 1
            while not formula[i] == '+':
                key += formula[i]
                i += 1
            if key in self.mp:
                a = self.mp[key]
            else:
                a = 0
        else:
            a = ord(formula[1]) - ord('0')
            i = 2
            while not formula[i] == '+':
                a = 10 * a + ord(formula[i]) - ord('0')
                i += 1
        i += 1
        if ord('A') <= ord(formula[i]) <= ord('Z'):
            key = ''
            while i < n:
                key += formula[i]
                i += 1
            if key in self.mp:
                b = self.mp[key]
            else:
                b = 0
        else:
            b = ord(formula[i]) - ord('0')
            i += 1
            while i < n:
                b = 10 * b + ord(formula[i]) - ord('0')
                i += 1
        return a + b
