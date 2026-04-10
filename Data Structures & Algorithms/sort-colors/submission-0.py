class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        counts = [0, 0, 0]
        for i in range(n):
            counts[nums[i]] += 1
        
        i = 0
        for x in range(3):
            for y in range(counts[x]):
                nums[i] = x
                i += 1