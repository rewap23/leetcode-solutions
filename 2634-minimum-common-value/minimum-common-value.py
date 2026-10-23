class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # if the problem mentions sorted, the binary search algorithm can be utilized
        # Binary Search Solution
        left = 0
        left2 = 0

        while left < len(nums1) and left2 < len(nums2):
            if nums1[left] == nums2[left2]:
                return nums1[left]
            elif nums1[left] < nums2[left2]:
                left += 1
            else:
                left2 += 1
        
        return -1