class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(logn)
        # vanilla binary search
        # cuts the searching in half every time
        # one pointer at the beginning and the end
        # and then the very middle
        # if the target value is greater than the middle value: we have to move the lower pointer to the number above the middle
        # if the target value is less than the middle value: we have to move the upper value down to the value one less than the middle 

        left = 0
        right = len(nums) - 1
        while left <= right:
            # mid
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
        