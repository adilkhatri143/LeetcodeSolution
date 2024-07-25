class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = list()
        num1_set = set(nums1)
        num2_set = set(nums2)
        answer.append(num1_set - num2_set)
        answer.append(num2_set - num1_set)
        return answer