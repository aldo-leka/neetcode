class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # not optimal cuz pop is o(n)
        # prev = -101 # invalid number 
        # for i in range(len(nums) - 1, -1, -1):
        #     #1,1,2,3,4
        #     #curr = 4
            
        #     curr = nums[i]
        #     # print(curr)
        #     # print(prev)
        #     if curr == prev:
        #         nums.pop(i)
        #     else:
        #         prev = curr
            
        # return len(nums)

        # optimal
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        
        return l