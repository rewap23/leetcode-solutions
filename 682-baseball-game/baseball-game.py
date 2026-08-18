class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        # stack solution
        # O(n) time
        # O(1) space
        points = [] # create stack of points
        for op in operations:
            if op == 'C': # if op is equal to C
                points.pop()
            elif op == 'D': # if op is equal to D
                points.append(points[-1] * 2)
            elif op == '+': # if op is equal to +
                points.append(points[-1] + points[-2])
            else:
                points.append(int(op)) # has to make sure it is an integer
        
        return sum(points) # return the sum of points