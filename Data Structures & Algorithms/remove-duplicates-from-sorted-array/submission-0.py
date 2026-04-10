class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = -101 # invalid number 
        for i in range(len(nums) - 1, -1, -1):
            #1,1,2,3,4
            #curr = 4
            
            curr = nums[i]
            # print(curr)
            # print(prev)
            if curr == prev:
                nums.pop(i)
            else:
                prev = curr
            
        return len(nums)