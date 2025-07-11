class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        time = [0] * n
        cnt = [0] * n
        for meeting in meetings:
            l = meeting[0]
            r = meeting[1]
            mintime = 10 ** 10
            minp = -1
            for i in range(n):
                if(time[i] <= l):
                    cnt[i] += 1
                    time[i] = r
                    minp = -1
                    break
                elif time[i] < mintime:
                    mintime = time[i]
                    minp = i
            if minp != -1:
                cnt[minp] += 1
                time[minp] += r - l
        ans = 0
        for i in range(n):
            if cnt[i] > cnt[ans]:
                ans = i
        return ans
