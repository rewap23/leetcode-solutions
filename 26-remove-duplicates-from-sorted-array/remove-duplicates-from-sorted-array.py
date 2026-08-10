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
                unique += 1
        return unique

