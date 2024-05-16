class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur_sum = 0
        no_of_subarray = 0
        for i in range(k):
            cur_sum += arr[i]
        if cur_sum // k >= threshold:
            no_of_subarray += 1
        for i in range(k, len(arr)):
            cur_sum -= arr[i - k]
            cur_sum += arr[i]
            if cur_sum // k >= threshold:
                no_of_subarray += 1
        return no_of_subarray

