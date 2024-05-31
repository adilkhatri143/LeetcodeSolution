class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        xor_val = 0
        for num in nums:
            xor_val ^= num
        set_bit_number = 1
        while xor_val & set_bit_number == 0:
            set_bit_number <<= 1
        group_a = 0
        group_b = 0
        for num in nums:
            if num & set_bit_number != 0:
                group_a ^= num
            else:
                group_b ^= num
        return [group_a, group_b]