nums = [8, 8, 7, 6, 5]
class Solution:
    def secondLargestElement(self, nums):
        if not nums:
            return -1
        uniq = sorted(set(nums))
        if len(uniq) < 2:
            return -1        
        return uniq[-2]  
    
    
solution = Solution 
print(solution().secondLargestElement(nums))