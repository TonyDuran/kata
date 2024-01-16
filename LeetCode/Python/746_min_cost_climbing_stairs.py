from typing import List
import pytest
test_cases = [
        (
        [10,15,20],
        15
        ),
        (
        [1,100,1,1,1,100,1,1,100,1],
        6
        ),
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().solution(test_input) == expected


class Solution:
    def solution(self, cost: List[int]) -> int:
        mem = {}
        def dp(i: int):
            if i <= 1:
                return 0
            if i not in mem:
                mem[i] = min(cost[i - 1] + dp(i - 1),cost[i - 2] + dp(i - 2) )
            return mem[i]
        return dp(len(cost))

