from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        max_r = len(maze) - 1
        max_c = len(maze[0]) - 1
        row_dir = [-1, 0, 1, 0]
        col_dir = [0, 1, 0, -1]
        q = deque()
        q.append(entrance)
        shortest_path = 0
        while q:
            size = len(q)
            while size:
                cur_row, cur_col = q.popleft()
                if not (cur_row == entrance[0] and cur_col == entrance[1]) and (cur_row == 0 or cur_row == max_r or cur_col == 0 or cur_col == max_c):
                    return shortest_path
                for row, col in zip(row_dir, col_dir):
                    new_row = cur_row + row
                    new_col = cur_col + col
                    if 0 <= new_row <= max_r and 0 <= new_col <= max_c and maze[new_row][new_col] != "+":
                        q.append([new_row, new_col])
                        # this is important step to avoid adding cell again to queue
                        maze[new_row][new_col] = "+"
                size -= 1
            shortest_path += 1
        return -1
