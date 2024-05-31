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
        first_single_number = 0
        second_single_number = 0
        for num in nums:
            if num & set_bit_number != 0:
                first_single_number ^= num
            else:
                second_single_number ^= num
        return [first_single_number, second_single_number]