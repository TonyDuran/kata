
# ====================
# Metadata: hint: yes, time: 45m, review: yes
# ====================

from typing import List
from functools import cache
import pytest
test_cases = [
        (
            ([9,9,9], 4),
            -1
        ),
        (
            ([1,1,1], 3),
            3
        ),
        (
            ([6,5,4,3,2,1], 2),
            7
        ),
        (
            ([1,5,4,100,2,200], 2),
            201
        ),
        (
            ([1,2,3,4,5,6], 2),
            7
        ),


]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().minDifficulty(*test_input) == expected


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int | float:
        if d > len(jobDifficulty):
            return -1
        elif d == len(jobDifficulty):
            return sum(jobDifficulty)

        hardest_job_remaining = [0] * len(jobDifficulty)
        hardest_job = 0
        for i in reversed(range(len(jobDifficulty))):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job

        @cache
        def dp(i, day):
            if day == d:
                return hardest_job_remaining[i]

            best = float("inf")
            hardest = 0
            for j in range(i, len(jobDifficulty) - (d - day)):
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j + 1, day + 1))
            return best

        return dp(0, 1)
