

nums = [3, 3, 0, 99, -40]

class Solution:
    def largestElement(self, nums):
        nums.sort()
        largest_number = max(nums)
        return largest_number



if __name__ == "__main__":
    print(Solution().largestElement(nums )) 
    