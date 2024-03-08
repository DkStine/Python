class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        while min(nums) != k:
            nums.remove(min(nums))
            count += 1
            
        return count
    

