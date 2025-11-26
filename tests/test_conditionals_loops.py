from __future__ import annotations

import importlib
import os

import pytest


USE_SOLUTIONS = os.getenv("USE_SOLUTIONS") == "1"
MODULE = importlib.import_module(
    "solutions.conditionals_loops_sols" if USE_SOLUTIONS else "problems.conditionals_loops"
)

cl_01_sum_even_up_to = MODULE.cl_01_sum_even_up_to
cl_02_product_multiples_range = MODULE.cl_02_product_multiples_range
cl_03_count_divisible = MODULE.cl_03_count_divisible
cl_04_first_index_gt = MODULE.cl_04_first_index_gt
cl_05_last_index_lt = MODULE.cl_05_last_index_lt
cl_06_has_adjacent_equal = MODULE.cl_06_has_adjacent_equal
cl_07_first_strict_increase_pair = MODULE.cl_07_first_strict_increase_pair
cl_08_longest_run_equal = MODULE.cl_08_longest_run_equal
cl_09_is_alternating_parity = MODULE.cl_09_is_alternating_parity
cl_10_first_violation_max_step = MODULE.cl_10_first_violation_max_step
cl_11_two_sum_exists = MODULE.cl_11_two_sum_exists
cl_12_sliding_window_max_sum = MODULE.cl_12_sliding_window_max_sum
cl_13_collatz_steps = MODULE.cl_13_collatz_steps
cl_14_gcd_euclid = MODULE.cl_14_gcd_euclid
cl_15_pow_int = MODULE.cl_15_pow_int
cl_16_sum_odd_indices = MODULE.cl_16_sum_odd_indices
cl_17_count_negatives_until_positive = MODULE.cl_17_count_negatives_until_positive
cl_18_first_prefix_sum_gt = MODULE.cl_18_first_prefix_sum_gt
cl_19_has_three_consecutive_increasing = MODULE.cl_19_has_three_consecutive_increasing
cl_20_min_subarray_len_at_least = MODULE.cl_20_min_subarray_len_at_least
cl_21_count_runs = MODULE.cl_21_count_runs
cl_22_index_of_min_even = MODULE.cl_22_index_of_min_even
cl_23_sum_every_kth = MODULE.cl_23_sum_every_kth
cl_24_move_zeros_right = MODULE.cl_24_move_zeros_right
cl_25_is_palindrome_list = MODULE.cl_25_is_palindrome_list
cl_26_running_maxima = MODULE.cl_26_running_maxima
cl_27_count_pairs_with_diff_at_most = MODULE.cl_27_count_pairs_with_diff_at_most
cl_28_has_two_adjacent_sum = MODULE.cl_28_has_two_adjacent_sum
cl_29_chunk_and_sum = MODULE.cl_29_chunk_and_sum
cl_30_count_valleys = MODULE.cl_30_count_valleys


def test_cl_01_sum_even_up_to_examples():
    assert cl_01_sum_even_up_to(6) == 12
    assert cl_01_sum_even_up_to(5) == 6
    assert cl_01_sum_even_up_to(-4) == -6
    assert cl_01_sum_even_up_to(-5) == -6


def test_cl_02_product_multiples_range_inclusive_and_reversed():
    assert cl_02_product_multiples_range(1, 10, 3) == 162
    assert cl_02_product_multiples_range(5, 7, 10) == 1
    assert cl_02_product_multiples_range(10, 1, 2) == 3840


def test_cl_02_product_multiples_range_rejects_zero_divisor():
    with pytest.raises(ValueError):
        cl_02_product_multiples_range(1, 5, 0)


def test_cl_03_count_divisible_counts_elements():
    assert cl_03_count_divisible([1, 2, 3, 4, 5, 6], 2) == 3
    assert cl_03_count_divisible([-3, -6, 5, 9], 3) == 3
    assert cl_03_count_divisible([], 7) == 0


def test_cl_03_count_divisible_zero_divisor():
    with pytest.raises(ValueError):
        cl_03_count_divisible([1, 2, 3], 0)


def test_cl_04_first_index_gt_found_and_missing():
    assert cl_04_first_index_gt([1, 2, 5, 3], 2) == 2
    assert cl_04_first_index_gt([5, 4, 3], 5) is None


def test_cl_05_last_index_lt_found_and_missing():
    assert cl_05_last_index_lt([3, 1, 4, 2], 3) == 3
    assert cl_05_last_index_lt([5, 6, 7], 5) is None


def test_cl_06_has_adjacent_equal_variants():
    assert cl_06_has_adjacent_equal([1, 2, 2, 3]) is True
    assert cl_06_has_adjacent_equal([1, 2, 3, 4]) is False
    assert cl_06_has_adjacent_equal([]) is False


def test_cl_07_first_strict_increase_pair_positions():
    assert cl_07_first_strict_increase_pair([5, 4, 6, 7]) == 1
    assert cl_07_first_strict_increase_pair([4, 3, 2]) is None
    assert cl_07_first_strict_increase_pair([10]) is None


def test_cl_08_longest_run_equal_handles_edges():
    assert cl_08_longest_run_equal([1, 1, 2, 2, 2, 3]) == 3
    assert cl_08_longest_run_equal([4, 4, 4, 4]) == 4
    assert cl_08_longest_run_equal([]) == 0


def test_cl_09_is_alternating_parity_cases():
    assert cl_09_is_alternating_parity([2, 3, 4, 5]) is True
    assert cl_09_is_alternating_parity([1, 3, 5]) is False
    assert cl_09_is_alternating_parity([7]) is True


def test_cl_10_first_violation_max_step_detects_breaks():
    assert cl_10_first_violation_max_step([1, 3, 7, 8], 3) == 2
    assert cl_10_first_violation_max_step([1, 2, 3, 5], 3) is None


def test_cl_11_two_sum_exists_true_and_false():
    assert cl_11_two_sum_exists([1, 2, 3, 4, 5], 9) is True
    assert cl_11_two_sum_exists([1, 2, 3], 7) is False
    assert cl_11_two_sum_exists([], 0) is False


def test_cl_12_sliding_window_max_sum_windows():
    assert cl_12_sliding_window_max_sum([1, 2, 3, 4, 5], 2) == 9
    assert cl_12_sliding_window_max_sum([5, 4, 3, 2, 1], 5) == 15
    assert cl_12_sliding_window_max_sum([-2, -1, -3, -4], 2) == -3


def test_cl_12_sliding_window_max_sum_invalid_k():
    with pytest.raises(ValueError):
        cl_12_sliding_window_max_sum([1, 2, 3], 0)
    with pytest.raises(ValueError):
        cl_12_sliding_window_max_sum([1, 2, 3], 4)


def test_cl_13_collatz_steps_examples_and_invalid():
    assert cl_13_collatz_steps(6, 10) == 8
    assert cl_13_collatz_steps(7, 5) == 5
    assert cl_13_collatz_steps(1, 10) == 0
    with pytest.raises(ValueError):
        cl_13_collatz_steps(0, 5)


def test_cl_14_gcd_euclid_negative_and_zero():
    assert cl_14_gcd_euclid(24, 18) == 6
    assert cl_14_gcd_euclid(-24, 18) == 6
    assert cl_14_gcd_euclid(0, 0) == 0


def test_cl_15_pow_int_cases_and_invalid():
    assert cl_15_pow_int(2, 3) == 8
    assert cl_15_pow_int(5, 0) == 1
    assert cl_15_pow_int(0, 5) == 0
    with pytest.raises(ValueError):
        cl_15_pow_int(2, -1)


def test_cl_16_sum_odd_indices():
    assert cl_16_sum_odd_indices([1, 2, 3, 4, 5]) == 6
    assert cl_16_sum_odd_indices([10]) == 0


def test_cl_17_count_negatives_until_positive_cases():
    assert cl_17_count_negatives_until_positive([-2, -1, 0, -5, 3]) == 3
    assert cl_17_count_negatives_until_positive([1, -1, -2]) == 0
    assert cl_17_count_negatives_until_positive([]) == 0


def test_cl_18_first_prefix_sum_gt_found_and_not():
    assert cl_18_first_prefix_sum_gt([1, 2, 3], 3) == 2
    assert cl_18_first_prefix_sum_gt([5], 10) is None


def test_cl_19_has_three_consecutive_increasing():
    assert cl_19_has_three_consecutive_increasing([5, 1, 2, 3, 0]) is True
    assert cl_19_has_three_consecutive_increasing([3, 2, 1, 0]) is False


def test_cl_20_min_subarray_len_at_least_cases():
    assert cl_20_min_subarray_len_at_least([2, 3, 1, 2, 4], 7) == 3
    assert cl_20_min_subarray_len_at_least([1, 1, 1], 5) is None
    assert cl_20_min_subarray_len_at_least([1, 2, 3], 0) == 0


def test_cl_21_count_runs_counts_groups():
    assert cl_21_count_runs([1, 1, 2, 2, 2, 3, 3, 1]) == 4
    assert cl_21_count_runs([]) == 0


def test_cl_22_index_of_min_even_cases():
    assert cl_22_index_of_min_even([5, 2, 4, 2]) == 1
    assert cl_22_index_of_min_even([1, 3, 5]) is None


def test_cl_23_sum_every_kth_and_invalid():
    assert cl_23_sum_every_kth([1, 2, 3, 4, 5], 2) == 9
    assert cl_23_sum_every_kth([10, 20], 3) == 10
    with pytest.raises(ValueError):
        cl_23_sum_every_kth([1, 2, 3], 0)


def test_cl_24_move_zeros_right_stable():
    assert cl_24_move_zeros_right([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert cl_24_move_zeros_right([]) == []


def test_cl_25_is_palindrome_list_cases():
    assert cl_25_is_palindrome_list([1, 2, 3, 2, 1]) is True
    assert cl_25_is_palindrome_list([1, 2, 3]) is False


def test_cl_26_running_maxima_outputs_prefix_max():
    assert cl_26_running_maxima([3, 1, 4, 2]) == [3, 3, 4, 4]
    assert cl_26_running_maxima([]) == []


def test_cl_27_count_pairs_with_diff_at_most_cases():
    assert cl_27_count_pairs_with_diff_at_most([1, 2, 4, 7], 2) == 2
    assert cl_27_count_pairs_with_diff_at_most([5, 5, 5], 0) == 3
    with pytest.raises(ValueError):
        cl_27_count_pairs_with_diff_at_most([1, 2, 3], -1)


def test_cl_28_has_two_adjacent_sum_true_false():
    assert cl_28_has_two_adjacent_sum([1, 3, 2, 4], 5) is True
    assert cl_28_has_two_adjacent_sum([1], 1) is False


def test_cl_29_chunk_and_sum_cases_and_invalid():
    assert cl_29_chunk_and_sum([1, 2, 3, 4, 5], 2) == [3, 7, 5]
    assert cl_29_chunk_and_sum([], 3) == []
    with pytest.raises(ValueError):
        cl_29_chunk_and_sum([1, 2], 0)


def test_cl_30_count_valleys_counts_and_validates():
    assert cl_30_count_valleys("UDDDUDUU") == 1
    assert cl_30_count_valleys("UUUDDD") == 0
    with pytest.raises(ValueError):
        cl_30_count_valleys("UDX")
