class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            seen=set()
            for num in board[i]:
                   if num=='.':
                           continue
                   if num in seen:
                            return False
                   seen.add(num)
            
        
        for j in range(len(board)):
            seen1=set()
            for i in range(len(board)):
                if board[i][j]=='.':
                           continue
                if board[i][j] in seen1:
                            return False
                seen1.add(board[i][j])
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen2=set()
        
                for row in range(i,i+3):
                    
                    for column in range(j,j+3):
                        if board[row][column]=='.':
                                    continue
                        if board[row][column] in seen2:
                                    return False
                        seen2.add(board[row][column])
        return True
