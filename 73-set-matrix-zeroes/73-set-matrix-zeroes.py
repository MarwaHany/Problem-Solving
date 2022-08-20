class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_flag = [None for element in matrix]
        col_flag = [None for li in matrix[0]]
        for i in range(len(row_flag)):
            for j in range(len(col_flag)):
                if not matrix[i][j]:
                    row_flag[i] = True
                    col_flag[j] = True
        cols_indeces = len(col_flag)
        for i in range(len(row_flag)):
            for j in range(cols_indeces):
                if row_flag[i] or col_flag[j]:
                    matrix[i][j] = 0
        del row_flag
        del col_flag
        del cols_indeces