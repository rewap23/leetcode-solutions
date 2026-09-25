class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pointer solution
        # O(1) space
        # O(n) time

        # setting a count variable to count how many letters are in the last work
        count = 0
        # setting a pointer so we can traverse from the end of the string
        end = len(s) - 1
        
        while end >= 0 and s[end] == ' ':
            end -= 1

        while end >= 0 and s[end] != ' ':
            count += 1
            end -= 1

        return count
