class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even = [0] * len(nums)
        odd = [0] * len(nums)
        even_sum = odd_sum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                even_sum += nums[i]
            else:
                odd_sum += nums[i]
            even[i] = even_sum
            odd[i] = odd_sum

        answer = 0
        for i in range(len(nums)):
            cur_even_sum = 0
            cur_odd_sum = 0
            if i == 0:
                cur_even_sum = odd[n - 1] - odd[i]
                cur_odd_sum = even[n - 1] - even[i]
            else:
                cur_even_sum = even[i - 1] + odd[n - 1] - odd[i]
                cur_odd_sum = odd[i - 1] + even[n - 1] - even[i]
            if cur_even_sum == cur_odd_sum:
                answer += 1
        return answer