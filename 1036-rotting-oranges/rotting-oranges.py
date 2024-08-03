class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        m = len(grid[0]) - 1
        q = deque()
        total_good_org = 0
        row_dir = [-1, 0, 1, 0]
        col_dir = [0, 1, 0, -1]
        for r in range(n + 1):
            for c in range(m + 1):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    total_good_org += 1
        minute = 0
        while q and total_good_org > 0:
            size = len(q)
            while size:
                cur_row, cur_col = q.popleft()
                for row, col in zip(row_dir, col_dir):
                    new_row = cur_row + row
                    new_col = cur_col + col
                    if 0 <= new_row <= n and 0 <= new_col <= m and grid[new_row][new_col] == 1:
                        q.append((new_row, new_col))
                        total_good_org -= 1
                        grid[new_row][new_col] = 2
                size -= 1 
            minute += 1
        return minute if total_good_org == 0 else -1