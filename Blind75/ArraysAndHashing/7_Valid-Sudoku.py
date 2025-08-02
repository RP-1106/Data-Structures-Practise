from collections import defaultdict

def find_value_in_d(d, num, i, j):
    box_row = i // 3
    box_col = j // 3

    for val_i, val_j in d[num]:
        # Check row or column conflict
        if val_i == i or val_j == j:
            return True

        # Check sub-box conflict
        if (val_i // 3 == box_row) and (val_j // 3 == box_col):
            return True
    return False

class Solution(object):
    def isValidSudoku(self, board):
        n = len(board)
        d = defaultdict(list)

        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num!=".":
                    if find_value_in_d(d, num, i,j ):
                        return False
                    else:
                        d[num].append([i,j])
        return True
