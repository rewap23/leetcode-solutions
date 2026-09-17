class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # OA prep
        # matrix problems

        # initializing rows and cols
        rows = len(matrix)
        cols = len(matrix[0])

        # initializing variables to check if a row or col is zero
        first_row_zero = False
        first_col_zero = False

        for m in range(rows):
            for n in range(cols): # always remember matrix[row variable][col variable]
                if matrix[m][n] == 0:
                    if m == 0:
                        first_row_zero = True
                    if n == 0:
                        first_col_zero = True
                    matrix[m][0] = 0 # updating those values to be zero if there is a zero
                    matrix[0][n] = 0     
        
        for m in range(1, rows):
            for n in range(1, cols):
                if matrix[m][0] == 0 or matrix[0][n] == 0: # if those updated values from above are zero we have to change the other values in the row to zero as well
                    matrix[m][n] = 0
                else:
                    matrix[m][n] = matrix[m][n]
        
        if first_row_zero:
            for n in range(cols):
                matrix[0][n] = 0
        if first_col_zero:
            for m in range(rows):
                matrix[m][0] = 0

        return matrix