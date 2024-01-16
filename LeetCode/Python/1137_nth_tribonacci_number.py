
import pytest
test_cases = [
        (4, 4),
        (25, 1_389_537)
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().tribonacci(test_input) == expected


class Solution:
    def tribonacci(self, n: int) -> int:
        mem = {}
        def dp(i):
            if i < 2:
                return i
            if i == 2:
                return 1
            if i not in mem:
                mem[i] = dp(i - 1) + dp(i - 2) + dp(i - 3)

            return mem[i]
        return dp(n)

