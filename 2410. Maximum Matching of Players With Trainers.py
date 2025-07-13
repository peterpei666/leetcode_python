class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = len(players) - 1
        j = len(trainers) - 1
        cnt = 0
        while i >= 0 and j >= 0:
            if players[i] <= trainers[j]:
                cnt += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        return cnt
