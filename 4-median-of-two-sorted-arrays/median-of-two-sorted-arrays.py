class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        low, high = 0, len(nums1)
        total_numbers_on_left = (m + n + 1) // 2
        while low <= high:
            mid = (low + high) // 2
            nums1_left = nums1[mid - 1] if mid > 0 else float('-inf')
            nums1_right = nums1[mid] if mid < len(nums1) else float('inf')
            nums2_left = nums2[total_numbers_on_left - mid - 1] if total_numbers_on_left - mid > 0 else float('-inf')
            nums2_right = nums2[total_numbers_on_left - mid] if total_numbers_on_left - mid < len(nums2) else float('inf')
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            if nums1_left < nums2_right:
                low = mid + 1
            else:
                high = mid - 1
        return 0