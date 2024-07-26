class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(ast):
                    stack.pop()
                if stack and stack[-1] == abs(ast):
                    stack.pop()
                elif not stack or (stack[-1] < 0):
                    stack.append(ast)
        return stack           