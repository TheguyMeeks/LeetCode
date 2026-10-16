class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                curr_box = boxes[row // 3][col // 3]

                if num == ".":
                    continue

                if (num in rows[row]) or (num in cols[col]) or (num in curr_box):
                    return False

                rows[row].add(num)
                cols[col].add(num)
                curr_box.add(num)

        return True
            