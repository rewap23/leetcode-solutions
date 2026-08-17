class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # O(n) time
        # O(1) space

        # storing change as 5s and 10s
        five = 0
        ten = 0
        for n in bills:
            if n == 5:
                five += 1
            if n == 10:
                if five == 0:
                    return False
                ten += 1
                five -= 1
            if n == 20:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True