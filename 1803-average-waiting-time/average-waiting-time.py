class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = waiting_time = 0
        for arr, time in customers:
            if arr < total_time:
                total_time += time
            else:
                total_time = arr + time
            waiting_time += (total_time - arr)
        return waiting_time / len(customers)