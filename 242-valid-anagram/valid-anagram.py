class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        #create hash map or dict for s and t 
        map_s = {}
        map_t = {}

        for char in s:
            map_s[char] = map_s.get(char, 0) + 1
        for char in t:
            map_t[char] = map_t.get(char, 0) + 1

        for key in map_s:
            if map_s[key] != map_t.get(key, 0):
                return False
        
        return True

        