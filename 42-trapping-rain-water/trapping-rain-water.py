class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # two pointers solution
        # O(n) time
        # O(1) space
        
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
            # if the left is smaller than the right
            if height[left] < height[right]:
                # then if the left is bigger than the max number of left, set the max number to left
                if height[left] >= leftMax:
                    leftMax = height[left]
                else: 
                    trapped_water += leftMax - height[left]
                left += 1
            # if the right is smaller than the left
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    trapped_water += rightMax - height[right]
                right -= 1
        
        return trapped_water