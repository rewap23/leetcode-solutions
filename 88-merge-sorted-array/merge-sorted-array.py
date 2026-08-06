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
        # solution should be stored in nums1 not returned
        # brute force - replacing index m onwards elements of nums1 with nums2
        #nums1[m:] = nums2
        #nums1.sort()
        # this isnt the best time complexity - calling .sort() function which is 
        # O(n log n)

        # best solution
        while (n-1) >= 0:
            if (m-1) >= 0 and (nums1[m-1] > nums2[n-1]):
                nums1[(m+n)-1] = nums1[m-1]
                m -= 1
            else:
                nums1[(m+n)-1] = nums2[n-1]
                n -= 1
            



        

        



        