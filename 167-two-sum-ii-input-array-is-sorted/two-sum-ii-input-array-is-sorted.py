class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # naive brute force approach would be to check every element and the next to see if the sum will equal target
        # what you can do is to have a pointer that moves 
        left = 0
        right = len(numbers) - 1

        while (left < right):
            if (numbers[left] + numbers[right]) == target:
                return [left+1, right+1]
            if (numbers[left] + numbers[right]) > target:
                right -= 1
            else:
                left += 1

