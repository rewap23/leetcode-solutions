class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # BFS - Binary Search 
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
                # return middle 
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # return left pointer 
        return left


        