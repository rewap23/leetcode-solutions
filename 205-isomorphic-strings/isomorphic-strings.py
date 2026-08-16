class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # O(n^2) time
        # 0(n) space
        sMap = []
        tMap = []

        for idx in s:
            sMap.append(s.index(idx)) # index function gets the index of that character
            # so for "egg" it looks at e and saves 0, and then looks at g and saves 1 and then 1 again bc it appears first at 1
        for idx in t:
            tMap.append(t.index(idx)) 
            # does the same logic as above
        if sMap == tMap:
            return True

        return False

