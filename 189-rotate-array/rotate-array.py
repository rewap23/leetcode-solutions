class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Reversing an Array Approach
        # O(n) time
        # O(1) space
        
        if len(nums) == 0:
            return 

        k = k % (len(nums))

        # write a reverse array function that we can reuse in this function because we have to reverse the entire array first, then reverse the first k elements, then reverse the elements after k
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
       
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)

            
        
        