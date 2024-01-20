
# ====================
# Metadata: hint: yes, time: 21m, review: yes, source: neetcode
# ====================
from typing import List
import pytest
test_cases = [
        (
            [100,4,200,1,3,2],
            4
        ),
        (
            [0,3,7,2,5,8,4,6,0,1],
            9
        )

]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().longestConsecutive(test_input) == expected


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest


