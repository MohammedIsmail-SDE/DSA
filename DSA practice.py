class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        
        # Iterate through the array with a right pointer
        for right in range(len(nums)):
            if nums[right] != 0:
                # Swap the non-zero element with the element at the left pointer
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
