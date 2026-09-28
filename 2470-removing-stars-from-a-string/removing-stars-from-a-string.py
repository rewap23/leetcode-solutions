class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Stack Solution
        result = []
        for char in s:
            # if the character equals * then we have to remove it
            if char == '*':
                result.pop()
            # if the character isn't a * we can add it to the result
            else:
                result+=[char]
        return ''.join(result)