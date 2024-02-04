
# ====================
# Metadata: hint: yes, time: 30m, review: yes
# ====================

from typing import List
import pytest

test_cases = [
        (
            [2,3,2],
            3
        ),
        (
            [1,2,3,1],
            4
        ),
        (
            [1,2,3],
            3
        ),
        (
        [200,3,140,20,10],
        340
        )

]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().rob(test_input) == expected


class Solution:
    def rob(self, nums: List[int]) -> int:
        def tabulate(num_list):
            rob1, rob2 = 0, 0
            for n in num_list:
                new_rob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2
        return max(nums[0], tabulate(nums[1:]), tabulate(nums[:-1]))
