
from typing import List
import pytest
test_cases = [
        (
        [1,2,3,1],
        4
        ),
        (
        [2,7,9,3,1],
        12
        ),
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().rob(test_input) == expected


class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in mem:
                mem[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return mem[i]
        return dp(len(nums) - 1)

