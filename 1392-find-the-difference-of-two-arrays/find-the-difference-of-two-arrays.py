class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # Sets/Hash Map Solution
        set1 = set(nums1) # sets prevent duplicates
        set2 = set(nums2)
        # initialize answer list
        answer = [[], []]
        for i in set1:
            if i not in set2:
                answer[0].append(i)
        for i in set2:
            if i not in set1:
                answer[1].append(i)
        return answer