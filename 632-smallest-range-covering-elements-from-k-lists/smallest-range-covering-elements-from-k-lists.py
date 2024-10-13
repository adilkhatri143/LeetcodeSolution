class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        heap = []
        min_max = [0, float("inf")]
        cur_max = float("-inf")
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            cur_max = max(cur_max, nums[i][0])
        
        while len(heap) == len(nums):
            cur_min, row, col = heapq.heappop(heap)

            if cur_max - cur_min < min_max[1] - min_max[0]:
                min_max[0] = cur_min
                min_max[1] = cur_max
            
            if col + 1 < len(nums[row]):
                next_val = nums[row][col + 1]
                heapq.heappush(heap, (next_val, row, col + 1))
                cur_max = max(cur_max, next_val)
    
        return min_max






        while True:
            cur_min, cur_max = float("inf"), float("-inf")
            min_value_index = 0
            for i in range(k):
                current_element = nums[i][cur_indices[i]]

                if current_element < cur_min:
                    cur_min = current_element
                    min_value_index = i
                if current_element > cur_max:
                    cur_max = current_element
                
            if cur_max - cur_min < range_list[1] - range_list[0]:
                range_list[0] = cur_min
                range_list[1] = cur_max
            
            cur_indices[min_value_index] += 1
            if cur_indices[min_value_index] == len(nums[min_value_index]):
                break
        return range_list