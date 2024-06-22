class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return [i for i in range(len(security))]
        n = len(security)
        non_increasing = [1] * n
        non_decreasing = [1] * n
        for i in range(1, n):
            if security[i - 1] >= security[i]:
                non_increasing[i] = non_increasing[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                non_decreasing[i] = non_decreasing[i + 1] + 1
        answer = list()
        print(non_increasing)
        print(non_decreasing)
        for i in range(time, n - time):
            if non_increasing[i] > time and non_decreasing[i] > time:
                answer.append(i)
        return answer

        
