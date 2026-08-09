class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # still have to use two pointer method
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skip_left = s[left+1:right+1]
                skip_right = s[left:right]
                reversed_sl = skip_left[::-1]
                reversed_sr = skip_right[::-1]
                return (skip_left == reversed_sl) or (skip_right == reversed_sr)
            left += 1
            right -= 1

        return True