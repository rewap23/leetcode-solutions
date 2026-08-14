class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # creating dict with key value pairs
        numsMap = defaultdict(int)

        for num in nums:
            numsMap[num] += 1

        # key is the number
        # value is the amount of times it appears
        for key, value in numsMap.items():
            if value > (len(nums) // 2):
                return key

        