class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        for i in range(len(positions)):
            positions[i] = (positions[i], healths[i], directions[i], i)
        positions.sort(key=lambda x: x[0])
        stack = list()
        for p, h, d, op in positions:
            if not stack:
                stack.append([h, d, op])
            elif stack and stack[-1][1] == "R" and d == "R":
                stack.append([h, d, op])
            elif stack and stack[-1][1] == "L" and d == "L":
                stack.append([h, d, op])
            elif stack and stack[-1][1] == "L" and d == "R":
                stack.append([h, d, op])
            else:
                to_add = False
                while stack and stack[-1][1] == "R" and d == "L":
                    if stack[-1][0] == h:
                        stack.pop()
                        to_add = False
                        break
                    elif stack[-1][0] > h:
                        stack[-1][0] -= 1
                        to_add = False
                        break
                    elif stack[-1][0] < h:
                        stack.pop()
                        h = h - 1
                        to_add = True
                if to_add:
                    stack.append([h, d, op])
        stack.sort(key=lambda k: k[2])
        return [h for h, d, op in stack]