class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        answer = list()
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                answer.append(stack[-1] - i)
            else:
                answer.append(0)
            stack.append(i)
        answer.reverse()
        return answer