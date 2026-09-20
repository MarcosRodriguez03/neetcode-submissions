class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        colSet = collections.defaultdict(set)
        rowSet = collections.defaultdict(set)
        boxSet = collections.defaultdict(set) # key = (r/3 , c/3)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in rowSet[i] or
                    board[i][j] in colSet[j] or 
                    board[i][j] in boxSet[(i//3 , j//3)]) :
                    return False
            
                colSet[j].add(board[i][j])
                rowSet[i].add(board[i][j])
                boxSet[i//3 , j // 3].add(board[i][j])
        return True