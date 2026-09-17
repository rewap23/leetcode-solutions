class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # OA prep
        # one line - transpose a matrix 
        # transpose = list(zip(*matrix))
        # new_mat = [
            #list(_) for _ in zip(*matrix)
        #]
        #return new_mat
        #initalize rows and columns of the matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # key thing to remember --> initalizing an resulting transposed matrix grid
        result = [[0] * rows for _ in range(cols)] 

        for i in range(cols):
            for j in range(rows):
                result[i][j] = matrix[j][i]

        return result

