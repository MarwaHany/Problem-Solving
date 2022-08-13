from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".": continue
                if ( 
                    board[row][col] in rows[row] 
                 or board[row][col] in cols[col]
                 or board[row][col] in square[(row//3,col//3)]
                ):
                    del(rows)
                    del(cols)
                    del(square)
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                square[(row//3,col//3)].add(board[row][col])
        
        del(rows)
        del(cols)
        del(square)
        return True
                