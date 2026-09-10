class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # base case if s is nothing it will always be a subsequence
        if not s:
            return True
        # base case, s cant be a subsequence if larger than t
        if len(s) > len(t):
            return False
        seen = 0 
        for char in t:
            if char == s[seen]:
                seen += 1
            if len(s) == seen:
                return True
        
        return seen == len(s)
        