class Solution:
    def get_count(self, target, nums):
        count = 0
        for num in nums:
            if num >= target:
                count += 1
        if count == target:
            return 0, target
        return -1, count

    def specialArray(self, nums: List[int]) -> int:
        # binary_search(0, max_num, nums)
        # for x in range(max_num + 1):
        #     count = 0
        #     for num in nums:
        #         if num >= x:
        #             count += 1
        #     if count == x:
        #         return 0, x
        # return -1, count
        max_num = max(nums)
        start = 0
        end = max_num
        while start <= end:
            mid = (start + end) // 2
            conti, answer = self.get_count(mid, nums)
            if conti != -1:
                return answer
            elif answer >= mid:
                start = mid + 1
            else:
                end = mid - 1
        return -1