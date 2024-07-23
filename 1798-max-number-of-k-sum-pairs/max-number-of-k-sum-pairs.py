class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_to_count = dict()
        for num in nums:
            num_to_count[num] = num_to_count.get(num, 0) + 1
        answer = 0
        for num in nums:
            if k - num in num_to_count:
                num_to_count[k - num] -= 1
                if num_to_count[k - num] <= 0:
                    num_to_count.pop(k - num)
                if num in num_to_count:
                    num_to_count[num] -= 1
                    if num_to_count[num] <= 0:
                        num_to_count.pop(num)
                    answer += 1
        return answer