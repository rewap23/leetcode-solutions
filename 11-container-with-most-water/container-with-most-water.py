class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # two pointers solution
        # O(n) time
        # O(1) space

        # base case 
        if not height:
            return 0
        
        # setting variables
        left = 0 #first
        right = len(height) - 1 #last
        maxWaterArea = 0
        currentArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right-left)
            maxWaterArea = max(maxWaterArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1

        return maxWaterArea
        


