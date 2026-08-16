class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #create hash map or dict for s and t 
        map_s = {}
        map_t = {}

        # case of s being empty
        if s == "":
            return t

        # adding all keys and values to hasp maps
        for char in s:
            map_s[char] = map_s.get(char, 0) + 1
        for char in t:
            map_t[char] = map_t.get(char, 0) + 1

        for key in map_t:
            if map_t[key] > map_s.get(key, 0) or map_t[key] != map_s.get(key, 0):
                return key