#!/usr/local/bin/python3
import os
file_name = input("what is the name of the challenge(please use snake_case): ")
challenge_number = input("What number challenge is this? Please use int: ")
input_str = """
// ====================
// Metadata: hint: yes|no, time: 15m, review: yes|no
// ====================


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_median_sorted_arrays_example1() {
        let nums1 = vec![1, 3];
        let nums2 = vec![2];
        let result = Solution::find_median_sorted_arrays(nums1, nums2);
        let expected = 2.0;
        assert_eq!(result, expected);
    }

    #[test]
    fn test_find_median_sorted_arrays_example2() {
        let nums1 = vec![1, 2];
        let nums2 = vec![3, 4];
        let result = Solution::find_median_sorted_arrays(nums1, nums2);
        let expected = 2.5;
        assert_eq!(result, expected);
    }
}

#[allow(dead_code)]
struct Solution;

impl Solution {
    #[allow(dead_code)]
    pub fn find_median_sorted_arrays(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> f64 {
    }
"""
# Get the current directory of the script
script_dir = os.path.dirname(__file__)
# Construct the path to the leet_code directory
leet_code_dir = os.path.join(script_dir, '..', 'LeetCode/Rust/src')
# Create the leet_code directory if it doesn't exist
os.makedirs(leet_code_dir, exist_ok=True)
# Construct the file path
file_path = os.path.join(leet_code_dir, f"{file_name}_{challenge_number}.rs")
lib_path = os.path.join(leet_code_dir, "lib.rs")

# Write to the file
with open(file_path, "w") as f:
    f.write(input_str)

with open(lib_path, "a") as f:
    f.write(f"mod {file_name}_{challenge_number};")

