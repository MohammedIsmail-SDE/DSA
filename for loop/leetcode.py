
class Solution:
    def (self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums