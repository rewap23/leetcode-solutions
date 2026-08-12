class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        i = 0
        for char in t:
            if i == len(s):
                return True
            if char == s[i]:
                i += 1
        
        return i == len(s)