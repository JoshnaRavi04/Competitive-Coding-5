# Time Complexity: O(m^3)
# Space Complexity: O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)

        for i in range(m):
            for j in range(m):
                val = board[i][j]
                if val == '.':
                    continue
                block_row = i // 3
                block_col = j // 3
                block_strow = block_row * 3
                block_stcol = block_col * 3

                count = 0
                for k in range(block_strow, block_strow + 3):
                    for l in range(block_stcol, block_stcol + 3):
                        if board[k][l] == val:
                            count += 1
                        if count > 1:
                            return False

                count = 0
                for a in range(m):
                    if board[i][a] == val:
                        count += 1
                    if count > 1:
                        return False

                count = 0
                for b in range(m):
                    if board[b][j] == val:
                        count += 1
                    if count > 1:
                        return False

        return True
