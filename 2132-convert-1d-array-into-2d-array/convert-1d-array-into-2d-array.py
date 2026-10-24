class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        # firstly check the base case: if the solution is k long, m*n must equal k
        if (m*n) != len(original):
            return []

        k = 0
        result = []

        for i in range(m):
            inside = []
            for j in range(n):
                inside.append(original[k])
                k+=1
            result.append(inside)

        return result
        

        