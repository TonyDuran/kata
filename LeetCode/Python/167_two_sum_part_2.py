
# ====================
# Metadata: hint: yes, time: 24m, review: yes
# ====================

from typing import List
import pytest
test_cases = [
        (
            ([2,7,11,15], 9),
            [1,2]
        ),
        (
            ([2,3,4], 6),
            [1,3]
        ),
        (
            ([-1,0], -1),
            [1,2]
        )
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().twoSum(*test_input) == expected


# This is a faster solution. I think O(log n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0
        r_ptr = len(numbers) - 1
        while l_ptr != r_ptr:
            if (numbers[l_ptr] + numbers[r_ptr]) > target:
                r_ptr -= 1
            elif (numbers[l_ptr] + numbers[r_ptr]) < target:
                l_ptr += 1
            else:
                return [l_ptr + 1, r_ptr + 1]
        return [0, 0]




# Attempt 1: Failed solution is too slow
# Assumption: Trying to brute-force without any caching. Not a good solution
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l_ptr = 0
#         r_ptr = len(numbers) - 1
#         while r_ptr > 0:
#             while l_ptr < r_ptr:
#                 if (numbers[l_ptr] + numbers[r_ptr]) == target:
#                     return [l_ptr + 1, r_ptr + 1]
#                 else:
#                     l_ptr += 1
#             r_ptr -= 1
#             l_ptr = 0
#         return[0, 0]

# Attempt 2: Successful, but still slow.
# Only watched the first 1 min of Neetcode's solution to realize I could break out of inner loop
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l_ptr = 0
#         r_ptr = len(numbers) - 1
#         while r_ptr > 0:
#             while l_ptr < r_ptr:
#                 if (numbers[l_ptr] + numbers[r_ptr]) == target:
#                     return [l_ptr + 1, r_ptr + 1]
#                 # NOTE: this speeds things up, but still slow solution
#                 elif (numbers[l_ptr] + numbers[r_ptr]) > target :
#                     break
#                 else:
#                     l_ptr += 1
#             r_ptr -= 1
#             l_ptr = 0
#         return[0, 0]


