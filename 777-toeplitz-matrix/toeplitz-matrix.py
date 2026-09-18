class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # OA Prep
        # O(n) time
        # O(1) space
        # initail these to be able to traverse through matrix
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r-1][c-1] != matrix[r][c]:
                    return False
        return True

