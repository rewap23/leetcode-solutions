class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 

        unique = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[unique] = nums[right] 
                #  This is the "in-place modification" step. It essentially shifts unique values to the front of the list, overwriting the unnecessary duplicate values that were previously sitting
                unique += 1
        return unique

