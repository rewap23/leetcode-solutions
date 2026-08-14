class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue # want to skip repeats
            left = i + 1
            right = len(nums) - 1
            while left < right:
                thrSum = num + nums[left] + nums[right]
                if thrSum > 0:
                    right -= 1
                elif thrSum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 
                    
        return result

