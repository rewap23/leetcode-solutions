class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        sumNums = sum(nums)
        difference = abs(goal - sumNums)
        return (difference + limit - 1) // limit
