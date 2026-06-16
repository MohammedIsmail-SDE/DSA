class Solution(object):
    def removeDuplicates(input):
        sorted_array =list(dict.fromkeys(input))
        return list(dict.fromkeys(input))
    
    
nums = [1,1,2]
print(Solution.removeDuplicates(nums))

while k:
            temp = nums.pop()
            nums.insert(0, temp)
            k -= 1