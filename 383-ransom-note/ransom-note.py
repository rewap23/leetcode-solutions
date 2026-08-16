class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # O(n) time
        # O(1) space

        # creating two hash maps 
        ransomMap = {}
        magazineMap = {}
        
        for char in ransomNote:
            ransomMap[char] = ransomMap.get(char, 0) + 1
        for char in magazine: 
            magazineMap[char] = magazineMap.get(char, 0) + 1
        
        for key in ransomMap:
            if magazineMap.get(key, 0) < ransomMap[key]:
                return False
        
        return True