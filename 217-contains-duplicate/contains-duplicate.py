class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsMap = defaultdict(int)

        for num in nums:
            numsMap[num] += 1

        for key, value in numsMap.items():
            if value >= 2:
                return True

        return False
        