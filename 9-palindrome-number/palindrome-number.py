class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False
        
        # two pointers solution
         #xlist = list(str(x)) 
        # base case scenario
        #if x < 0:
            #return False
        #right = len(xlist) - 1
        #for left in range(len(xlist)):
            #xlist[left] = xlist[right]
            #xlist[right] = xlist[left]
            #right -= 1
        #if "".join(xlist) == str(x):
            #return True
        #else: 
            #return False