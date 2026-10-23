class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # hashset solution
        # create a set and add all elements of numss1
        # since the elements are already sorted, this will automatically return the first same value which will be the min same value
        # traverse through nums2 and if it exists in nums1 return it or else return -1
        # O(n) space and time
        seen = set(nums1)

        for num in nums2:
            if num in seen:
                return num
                break
        return -1

        
