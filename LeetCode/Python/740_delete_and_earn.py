from collections import Counter
from typing import List
import pytest
test_cases = [
        (
            [3,4,2],
            6
        ),
        (
            [2,2,3,3,3,4],
            9
        )
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().deleteAndEarn(test_input) == expected


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]
            # checks if the number is consecutive
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
        return earn2

