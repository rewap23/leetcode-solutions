class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # O(n) time complexity
        # O(1) space complexity
        numsMap = {} # tracking the number of times a number is in the nums1
        output = []
        
        for num in nums1: # counting the number and the amount of times it appears
            numsMap[num] = numsMap.get(num, 0) + 1

        for num in nums2:
            if num in numsMap and numsMap[num] > 0:
                output.append(num)
                numsMap[num] -= 1

        return output

        