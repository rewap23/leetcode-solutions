class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        # stack solution
        # O(n) time
        # O(1) space
        stack = []
        for log in logs:
            if log == '../': 
                if stack: # can only pop from stack if its not empty
                    stack.pop()
                else: # if stack empty you have to continue
                    continue
            elif log == './':
                continue # you do nothing so you continue
            else:
                stack.append(log)

        return len(stack) # return the number of logs