class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # simple while loop approach but a lot of lines of code
        left = 0
        right = len(s)
        result = 0
        
        while left < right:
            if s[left] == 'M':
                result += 1000
            elif s[left] == 'D':
                result += 500
            elif s[left] == 'L':
                result += 50
            elif s[left] == 'V':
                result += 5
            elif s[left] == 'I':
                if left+1 < right and s[left+1] == 'V':
                    result += 4
                    left += 1
                elif left+1 < right and s[left+1] == 'X':
                    result += 9
                    left += 1
                else:
                    result += 1
            elif s[left] == 'X':
                if left+1 < right and s[left+1] == 'L':
                    result += 40
                    left += 1
                elif left+1 < right and s[left+1] == 'C':
                    result += 90
                    left += 1
                else:
                    result += 10
            elif s[left] == 'C':
                if left+1 < right and s[left+1] == 'D':
                    result += 400
                    left += 1
                elif left+1 < right and s[left+1] == 'M':
                    result += 900
                    left += 1
                else:
                    result += 100
            left += 1
        
        return result