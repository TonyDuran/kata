from typing import List
from functools import lru_cache
import pytest
test_cases = [
        (
            ([3,2,1], [3,2,1]),
            14
        ),
        (
            ([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]),
            102
            )
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().maximumScore(*test_input) == expected


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        @lru_cache(2000)
        def dp(i, left):
            if i == m:
                return 0

            mult = multipliers[i]
            right = n - 1 - (i - left)
            return max(mult * nums[left] + dp(i + 1, left + 1),
                       mult * nums[right] + dp(i + 1, left))


        n, m = len(nums), len(multipliers)
        return dp(0,0)

