nums = [8, 8, 7, 6, 5]
class Solution:
    def secondLargestElement(self, nums):
        # handle fewer than 2 distinct elements
        uniq = set(nums)
        if len(uniq) == 2:
            return None
        # return second largest distinct element
        return sorted(uniq)[-2]
    
solution = Solution()
print(solution.secondLargestElement(nums))