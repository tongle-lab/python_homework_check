"""valid_sudoku 模块的单元测试。"""

import sys
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from valid_sudoku import Solution


class TestValidSudoku(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_valid_partially_filled_board(self) -> None:
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertTrue(self.solution.isValidSudoku(board))

    def test_invalid_duplicate_in_row(self) -> None:
        board = [["."] * 9 for _ in range(9)]
        board[0][0] = "5"
        board[0][8] = "5"
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_invalid_duplicate_in_column(self) -> None:
        board = [["."] * 9 for _ in range(9)]
        board[0][0] = "7"
        board[8][0] = "7"
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_invalid_duplicate_in_box(self) -> None:
        board = [["."] * 9 for _ in range(9)]
        board[0][0] = "9"
        board[2][2] = "9"
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_empty_board_is_valid(self) -> None:
        board = [["."] * 9 for _ in range(9)]
        self.assertTrue(self.solution.isValidSudoku(board))

    def test_valid_completed_board(self) -> None:
        board = [
            list("534678912"),
            list("672195348"),
            list("198342567"),
            list("859761423"),
            list("426853791"),
            list("713924856"),
            list("961537284"),
            list("287419635"),
            list("345286179"),
        ]
        self.assertTrue(self.solution.isValidSudoku(board))


if __name__ == "__main__":
    unittest.main(verbosity=2)
