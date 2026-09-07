class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # two pointers solution
        # O(n) time
        # O(1) space
        # start by initializing a point to the beginning of the string and the end of the string
        left = 0
        right = len(s) - 1
        # only can do these operations as long as left is less than or equal to right
        while left <= right:
            # swap the left and right values
            s[left], s[right] = s[right], s[left]
            # increment left by 1 to move on to the next element
            # decrement right by 1 to move to the previous element
            left += 1
            right -= 1
        # return the string
        return s