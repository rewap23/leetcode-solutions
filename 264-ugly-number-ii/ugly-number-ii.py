class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Three Pointers - Dynamic Programming
        uglyNum = [0] * n
        uglyNum[0] = 1

        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            next2 = uglyNum[p2] * 2
            next3 = uglyNum[p3] * 3
            next5 = uglyNum[p5] * 5
            
            # next ugly number is the smallest of them all
            next_ugly = min(next2, next3, next5)
            uglyNum[i] = next_ugly

            if next_ugly == next2:
                p2 += 1
            if next_ugly == next3:
                p3 += 1
            if next_ugly == next5:
                p5 += 1
                
        return uglyNum[-1]

