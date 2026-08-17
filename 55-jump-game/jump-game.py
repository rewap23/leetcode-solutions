class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # two pointers but only one pointer and looping through with the other pointer
        # O(n) time
        # O(1) space
        
        left = 0

        for right in range(len(nums)):
            if right > left:
                return False
            left = max(left, right + nums[right])

        return True
            