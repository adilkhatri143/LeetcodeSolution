class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum_to_count = {0: 1}
        cur_sum = ans = 0
        for idx, num in enumerate(nums):
            cur_sum += num
            rem = cur_sum % k
            if rem in sum_to_count:
                ans += sum_to_count[rem]
                sum_to_count[rem] += 1
            else:
                sum_to_count[rem] = 1
        return ans