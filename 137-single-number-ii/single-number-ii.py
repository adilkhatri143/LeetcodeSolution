import ctypes
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            temp = 1 << i
            zero_count, one_count = 0, 0
            for num in nums:
                if num & temp == 0:
                    zero_count += 1
                else:
                    one_count += 1
            if one_count % 3 == 1:
                result = result | temp
        return ctypes.c_int32(result).value

