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
        let total_size = nums1.len() + nums2.len();
        let is_odd = total_size % 2 != 0;
        let median = if is_odd {
            total_size / 2
        } else {
            (total_size / 2) - 1
        };

        let mut idx = 0;
        while idx <= median {
            let curr_num_one = nums1.get(0).cloned().unwrap_or(i32::MAX);
            let curr_num_two = nums2.get(0).cloned().unwrap_or(i32::MAX);

            if idx == median {
                if is_odd {
                    return curr_num_one.min(curr_num_two) as f64;
                } else {
                    let val_one = if curr_num_one < curr_num_two {
                        nums1.remove(0)
                    } else {
                        nums2.remove(0)
                    };

                    let curr_num_one = nums1.get(0).cloned().unwrap_or(i32::MAX);
                    let curr_num_two = nums2.get(0).cloned().unwrap_or(i32::MAX);
                    let val_two = curr_num_one.min(curr_num_two);

                    return (val_one + val_two) as f64 / 2.0;
                }
            }

            if curr_num_one < curr_num_two {
                nums1.remove(0);
            } else {
                nums2.remove(0);
            }
            idx += 1;
        }
        0.0
    }
}

