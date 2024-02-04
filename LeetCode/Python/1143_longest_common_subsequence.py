
# ====================
# Metadata: hint: yes, time: 1h, review: very_much
# ====================

from functools import lru_cache
from typing import List
import pytest
test_cases = [
        (
            ["abcde", "ace"],
            3
        ),
        (
            ["abc", "abc"],
            3
        ),
        (
            ["abc", "def"],
            0
        ),
        (
            ["psnw", "vozsh"],
            1
        )

]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().longestCommonSubsequence(*test_input) == expected


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):

            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Recursive case 1.
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)

            # Recursive case 2.
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))

        return memo_solve(0, 0)
