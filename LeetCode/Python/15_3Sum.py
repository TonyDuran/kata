
# ====================
# Metadata: hint: yes, time: 30m, review: yes
# ====================

from typing import List
import pytest
test_cases = [
    (
        [-1,0,1,2,-1,-4],
        [[-1,-1,2],[-1,0,1]]
    ),
    (
        [0,1,1],
        []
    ),
    (
        [0,0,0],
        [[0,0,0]]
    ),


]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().threeSum(test_input) == expected


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            lptr, rptr = i + 1, len(nums) - 1
            while lptr < rptr:
                three_sum = a + nums[lptr] + nums[rptr]
                if three_sum > 0:
                    rptr -= 1
                elif three_sum < 0:
                    lptr += 1
                else:
                    res.append([a, nums[lptr], nums[rptr]])
                    lptr += 1
                    while nums[lptr] == nums[lptr - 1] and lptr < rptr:
                        lptr += 1

        return res
