
# ====================
# Metadata: hint: no, time: 1h, review: no
# ====================

from typing import List
import pytest
from math import floor
test_cases = [
        (
            ([1,3], [2]),
            2
        ),
        (
            ([1,2],[3,4]),
            2.5
        ),
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().findMedianSortedArrays(*test_input) == expected


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_size = len(nums1) + len(nums2)
        is_odd = bool(total_size % 2)
        if is_odd:
            median = floor(total_size / 2)
        else:
            median = (floor(total_size / 2)) - 1

        idx = 0
        while idx <= median:
            curr_num_one = float('inf')
            curr_num_two = float('inf')
            if nums1:
                curr_num_one = nums1[0]
            if nums2:
                curr_num_two = nums2[0]

            if idx == median:
                if is_odd:
                    return curr_num_one if curr_num_one < curr_num_two else curr_num_two
                else:
                    val_one = nums1.pop(0) if curr_num_one < curr_num_two else nums2.pop(0)
                    curr_num_one = float('inf')
                    curr_num_two = float('inf')
                    if nums1:
                        curr_num_one = nums1.pop(0)
                    if nums2:
                        curr_num_two = nums2.pop(0)
                    val_two = curr_num_one if curr_num_one < curr_num_two else curr_num_two
                    return (val_one + val_two) / 2

            nums1.pop(0) if curr_num_one < curr_num_two else nums2.pop(0)
            idx += 1
        return 0
