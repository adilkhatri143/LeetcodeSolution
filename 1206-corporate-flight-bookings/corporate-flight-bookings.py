class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * n
        for first, last, seat in bookings:
            answer[first - 1] += seat
            if last < n:
                answer[last] -= seat
        
        for i in range(1, len(answer)):
            answer[i] += answer[i - 1]
        return answer