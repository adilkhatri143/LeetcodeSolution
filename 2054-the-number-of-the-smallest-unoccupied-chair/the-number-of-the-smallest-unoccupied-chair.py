class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i in range(len(times)):
            times[i] = [times[i][0], times[i][1], i]
        times.sort(key=lambda x: x[0])
        current_chair = 0
        leaving = []
        available_chair = []
        for i in range(len(times)):
            arr, dep, idx = times[i]
            while leaving and leaving[0][0] <= arr:
                dep_time, chair = heapq.heappop(leaving)
                heapq.heappush(available_chair, chair)
            
            if available_chair:
                chair = heapq.heappop(available_chair)
                heapq.heappush(leaving, [dep, chair])
                if idx == targetFriend:
                    return chair
            else:
                heapq.heappush(leaving, [dep, current_chair])
                if idx == targetFriend:
                    return current_chair
                current_chair+= 1
