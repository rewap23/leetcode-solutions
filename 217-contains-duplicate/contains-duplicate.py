class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # same idea as majority element
        # creating dictionary and storing the number and the amount of times it appears
        numsMap = defaultdict(int)

        for num in nums:
            numsMap[num] += 1

        for key, value in numsMap.items():
            if value >= 2:
                return True

        return False
        