class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cntA = cntB = 0
        tempA = tempB = 0
        for i in range(len(colors)):
            if colors[i] == 'A':
                tempA += 1
                if tempB >= 3:
                    cntB += tempB - 2
                tempB = 0
            else:
                tempB += 1
                if tempA >= 3:
                    cntA += tempA - 2
                tempA = 0
        if tempA >= 3:
            cntA += tempA - 2
        if tempB >= 3:
            cntB += tempB - 2
        return cntA > cntB
