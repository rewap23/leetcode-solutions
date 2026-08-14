class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numsMap = {}

        for num in range(len(nums)):
            if nums[num] in numsMap and abs(num - numsMap[nums[num]]) <= k:
                return True
            numsMap[nums[num]] = num

        return False
