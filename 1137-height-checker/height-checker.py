class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count_heights = [0] * 101
        cur_height = answer = 0
        for height in heights:
            count_heights[height] += 1
        for height in heights:
            while count_heights[cur_height] == 0:
                cur_height += 1
            if cur_height != height:
                answer += 1
            count_heights[cur_height] -= 1
        return answer