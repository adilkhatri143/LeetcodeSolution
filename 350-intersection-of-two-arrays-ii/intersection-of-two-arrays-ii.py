class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_map = dict()
        for num in nums1:
            num1_map[num] = num1_map.get(num, 0) + 1
        answer = list()
        for num in nums2:
            if num in num1_map:
                answer.append(num)
                num1_map[num] = num1_map.get(num) - 1
                if not num1_map[num]:
                    num1_map.pop(num)
        return answer