#!/usr/local/bin/python3
import os
file_name = input("what is the name of the challenge(please use snake_case): ")
challenge_number = input("What number challenge is this? Please use int: ")
input_str = f"""
# ====================
# Metadata: hint: yes|no, time: 15m, review: yes|no
# ====================

from typing import List
import pytest
test_cases = [
        (0, 1),
        (4, 5),
        (
            [0,1,2],
            12
        )
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_scenarios(test_input, expected):
    assert Solution().solution(test_input) == expected


class Solution:
    def solution(self, args):
        pass

"""
# Get the current directory of the script
script_dir = os.path.dirname(__file__)
# Construct the path to the leet_code directory
leet_code_dir = os.path.join(script_dir, '..', 'LeetCode/Python')
# Create the leet_code directory if it doesn't exist
os.makedirs(leet_code_dir, exist_ok=True)
# Construct the file path
file_path = os.path.join(leet_code_dir, f"{challenge_number}_{file_name}.py")

# Write to the file
with open(file_path, "x") as f:
    f.write(input_str)

