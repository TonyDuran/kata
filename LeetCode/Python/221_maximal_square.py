
# ====================
# Metadata: hint: yes, time: 20m, review: yes
# ====================

from typing import List
import pytest
from functools import cache
test_cases = [
        (
            [["1","0","1","1","1"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],
            9
        ),
        (
            [["0","1"],["1","0"]],
            1
        ),
        (
            [["0"]],
            0
        )

]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().maximalSquare(test_input) == expected


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)
            return cache[(r, c)]
        helper(0, 0)
        return max(cache.values()) ** 2

