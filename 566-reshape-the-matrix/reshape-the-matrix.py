class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])

        # create a grid of the dimensions of the new matrix
        result = [[0] * c for _ in range(r)]

        if (rows * cols) != (r * c):
            return mat
        
        for i in range(rows * cols):
            result[i // c][i % c] = mat[i // cols][i % cols]
                
        return result


