class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMap = []
        tMap = []

        for idx in s:
            sMap.append(s.index(idx))
        for idx in t:
            tMap.append(t.index(idx))

        if sMap == tMap:
            return True

        return False

