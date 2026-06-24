class Solution:
    def linearSearch( nums, target):
        for i in range(len(nums)):
            if nums[i] == target :
                return i
        return -1 
    
    
nums = [1,2,3,4,5,6]
target = 3

value = Solution.linearSearch(nums,target)
print(value)
        