class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # result needs to be a string
        result = ""
        for char in s:
            if char == "i":
                result = result[::-1] # this is o(n) time, reverses a string
            else:
                result += char
        return result
                