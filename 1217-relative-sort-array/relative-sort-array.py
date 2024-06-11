class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_num = max(arr1)
        count_num = [0] * (max_num + 1)
        for num in arr1:
            count_num[num] += 1
        final_ans = list()
        for num in arr2:
            while count_num[num] != 0:
                final_ans.append(num)
                count_num[num] -= 1
        for i in range(len(count_num)):
            while count_num[i] != 0:
                final_ans.append(i)
                count_num[i] -= 1
        return final_ans