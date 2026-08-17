class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # two pointers solution
        
        # base case
        if not height or len(height) < 3:
            return 0

        # we want to know how much water a structure could trap given the height
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        trapped_water = 0

        # find the minimum of left and right
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else: 
                    trapped_water += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    trapped_water += rightMax - height[right]
                right -= 1
        
        return trapped_water