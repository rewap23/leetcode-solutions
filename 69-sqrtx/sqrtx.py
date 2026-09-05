class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # simple math approach
        # O(n) time
        # O(1) space

        num = 1
        while (num * num) <= x:
            num += 1
        # round down not up
        return num - 1
