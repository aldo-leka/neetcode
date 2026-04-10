class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        n = len(nums)
        k = n
        while l < k:
            # shift all right to left
            if nums[l] == val:
                r = l + 1
                while r < n:
                    nums[r - 1] = nums[r]
                    r += 1
                k -= 1
            else:
                l += 1
            
        return k