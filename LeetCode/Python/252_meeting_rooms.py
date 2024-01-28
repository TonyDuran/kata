
# ====================
# Metadata: hint: no, time: 40m, review: yes
# ====================

from typing import List
import pytest
test_cases = [
        (
            [[0,30],[5,10],[15,20]],
            False,
        ),
        (
            [[7,10],[2,4]],
            True
        )
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().canAttendMeetings(test_input) == expected


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #sort by start_time
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        for idx, meeting in enumerate(sorted_intervals):
            if idx + 1 > len(sorted_intervals) - 1:
                break
            if meeting[1] > sorted_intervals[idx+1][0]:
                return False

        return True
