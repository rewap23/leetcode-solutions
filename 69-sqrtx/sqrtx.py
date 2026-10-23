class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = 0
        right = x // 2

        while left <= right:
            mid = (left+right)//2
            squared = mid * mid
            if squared == x:
                return mid
            elif squared > x:
                right = mid - 1
            else:
                left = mid + 1

        return right
                

