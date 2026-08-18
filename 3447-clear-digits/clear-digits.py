class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # stack solution
        # O(n) time
        # O(n) space
        stack = []
        for char in s:
            if '0' <= char <= '9': # if char is a digit
                if stack: # can only pop if stack is true
                    stack.pop()
                else:
                    continue
            else:
                stack.append(char)
        
        return ''.join(stack)
