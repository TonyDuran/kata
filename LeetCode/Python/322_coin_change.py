
# ====================
# Metadata: hint: yes, time: 40m, review: yes
# ====================

from typing import List
from functools import cache
import pytest
test_cases = [
        (
            ([1,2,5], 11),
            3
        ),
        (
            ([2], 3),
            -1
        ),
        (
            ([1], 0),
            0
        )


]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().coinChange(*test_input) == expected


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
