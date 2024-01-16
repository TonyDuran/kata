
import pytest
test_cases = [
        (2, 2),
        (3, 3),
        (44, 1134903170)
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().climbStairs(test_input) == expected

class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def dp(i):
            if i <= 2:
                return i
            if i not in mem:
                mem[i] = dp(i - 1) + dp(i - 2)
            return mem[i]
        return dp(n)


