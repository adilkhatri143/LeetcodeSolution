class Solution:
    def merge(self, nums, left, mid, right):
        left_arr = [0] * (mid - left + 1)
        right_arr = [0] * (right - mid)

        for i in range(mid - left + 1):
            left_arr[i] = nums[left + i]
        for i in range(right - mid):
            right_arr[i] = nums[mid + i + 1]
        
        left_ptr = right_ptr = 0
        merge_ptr = left
        while left_ptr < len(left_arr) and right_ptr < len(right_arr):
            if left_arr[left_ptr] < right_arr[right_ptr]:
                nums[merge_ptr] = left_arr[left_ptr]
                left_ptr += 1
            else:
                nums[merge_ptr] = right_arr[right_ptr]
                right_ptr += 1
            merge_ptr += 1
        
        while left_ptr < len(left_arr):
            nums[merge_ptr] = left_arr[left_ptr]
            left_ptr += 1
            merge_ptr += 1
        
        while right < len(right_arr):
            nums[merge_ptr] = right_arr[right_ptr]
            right_ptr += 1
            merge_ptr += 1        

    def merge_sort(self, nums, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(nums, left, mid)
            self.merge_sort(nums, mid + 1, right)
            return self.merge(nums, left, mid, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        self.merge_sort(nums, left, right)
        return nums