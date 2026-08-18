class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        # use a stack to keep track of asteroids
        # the order of the other asteroids needs to be preserved
        for ast in asteroids:
            # for every asteroid we can only do collisions if an asteriod is moving to the left and another is moving to the right
            while stack and ast < 0 and stack[-1] > 0:
                diff = ast + stack[-1]
                if diff < 0:
                    # negative is bigger than postitive
                    stack.pop()
                elif diff > 0:
                    ast = 0
                else:
                    ast = 0
                    stack.pop()
            if ast:
                stack.append(ast)

        return stack

