class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # O(1) time
        # O(1) space
        # if a player has an even number they win
        # so if Alice has an even number she wins
        if n % 2 == 0:
            return True
        else:
            return False
