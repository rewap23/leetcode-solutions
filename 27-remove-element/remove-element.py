class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        result = 0
        for num in range(len(nums)):
            if nums[num] != val:
                nums[result] = nums[num]
                result += 1
        return result
  