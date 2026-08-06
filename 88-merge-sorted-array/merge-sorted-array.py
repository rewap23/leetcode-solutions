class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # taking four parameters - two arrays, two integers that are the number of elements in the arrays we are adding
        
        # brute force - replace the 
        nums1[m:] = nums2
        nums1.sort()
        



        