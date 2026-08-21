class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bit manipulation
        # O(n) time
        # 0(1) space

        result = 0
        while n != 0:
            result += 1
            n = n & (n-1)
            # decrementing number by 1 so there is one less one each time

        return result