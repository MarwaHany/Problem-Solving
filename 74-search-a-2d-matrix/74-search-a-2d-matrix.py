class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # to search in a matrix using binary search 
        # row = index // 2
        # col = index % 2
        start = 0
        col_len = len(matrix[0])
        end = len(matrix) * col_len
        while start < end:
            mid = (start + end) // 2
            if matrix [mid//col_len][mid%col_len] == target:
                return True
            elif target < matrix[mid//col_len][mid%col_len]:
                end = mid
            else:
                start = mid + 1
        return False
