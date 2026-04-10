class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1_idx, nums2_idx = 0, 0
        for i in range(m):
            for j in range(n):
                if nums1[i] > nums2[j]:
                    nums1[i], nums2[j] = nums2[j], nums1[i]
            print(nums1)
        smallest_idx = 0
        idx = m
        while len(nums2):
            for i in range(len(nums2)):
                if nums2[i] < nums2[smallest_idx]:
                    smallest_idx = i
            nums1[idx] = nums2[smallest_idx]
            nums2.pop(smallest_idx)
            smallest_idx = 0
            idx += 1

