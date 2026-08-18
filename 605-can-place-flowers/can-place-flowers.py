class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # two pointers solution method
        # O(n) time
        # O(1) space

        # base case
        if n == 0:
            return True

        left = 0
        right = len(flowerbed)

        while left < right:
            if flowerbed[left] == 1:
                left += 2
            elif left == right - 1 or flowerbed[left + 1] == 0:
                n -= 1
                left += 2
            else:
                left += 3

        return n <= 0



