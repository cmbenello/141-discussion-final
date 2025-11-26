from __future__ import annotations

import importlib
import os

import pytest


USE_SOLUTIONS = os.getenv("USE_SOLUTIONS") == "1"
MODULE = importlib.import_module(
    "solutions.recursion_lists_sols" if USE_SOLUTIONS else "problems.recursion_lists"
)


rl_01_len_recursive = MODULE.rl_01_len_recursive
rl_02_sum_recursive = MODULE.rl_02_sum_recursive
rl_03_count_occurrences = MODULE.rl_03_count_occurrences
rl_04_contains = MODULE.rl_04_contains
rl_05_all_positive = MODULE.rl_05_all_positive
rl_06_any_negative = MODULE.rl_06_any_negative
rl_07_max_recursive = MODULE.rl_07_max_recursive
rl_08_min_recursive = MODULE.rl_08_min_recursive
rl_09_index_of_first = MODULE.rl_09_index_of_first
rl_10_index_of_last = MODULE.rl_10_index_of_last
rl_11_copy_list = MODULE.rl_11_copy_list
rl_12_reverse_new = MODULE.rl_12_reverse_new
rl_13_increment_all = MODULE.rl_13_increment_all
rl_14_filter_even = MODULE.rl_14_filter_even
rl_15_remove_target = MODULE.rl_15_remove_target
rl_16_take_first_n = MODULE.rl_16_take_first_n
rl_17_drop_first_n = MODULE.rl_17_drop_first_n
rl_18_concat_lists = MODULE.rl_18_concat_lists
rl_19_interleave_recursive = MODULE.rl_19_interleave_recursive
rl_20_flatten_shallow = MODULE.rl_20_flatten_shallow
rl_21_binary_search_recursive = MODULE.rl_21_binary_search_recursive
rl_22_merge_two_sorted_recursive = MODULE.rl_22_merge_two_sorted_recursive
rl_23_merge_sort_recursive = MODULE.rl_23_merge_sort_recursive
rl_24_is_sorted_recursive = MODULE.rl_24_is_sorted_recursive
rl_25_count_inversions_simple = MODULE.rl_25_count_inversions_simple
rl_26_count_smaller_to_right = MODULE.rl_26_count_smaller_to_right
rl_27_max_subarray_sum_simple = MODULE.rl_27_max_subarray_sum_simple
rl_28_split_even_odd_indices = MODULE.rl_28_split_even_odd_indices
rl_29_find_min_max_recursive = MODULE.rl_29_find_min_max_recursive
rl_30_rotate_left_recursive = MODULE.rl_30_rotate_left_recursive
rl_31_len_from_index = MODULE.rl_31_len_from_index
rl_32_sum_from_index = MODULE.rl_32_sum_from_index
rl_33_is_palindrome_list = MODULE.rl_33_is_palindrome_list
rl_34_lists_equal = MODULE.rl_34_lists_equal
rl_35_zip_lists_recursive = MODULE.rl_35_zip_lists_recursive
rl_36_unzip_pairs_recursive = MODULE.rl_36_unzip_pairs_recursive
rl_37_all_prefixes = MODULE.rl_37_all_prefixes
rl_38_all_suffixes = MODULE.rl_38_all_suffixes
rl_39_split_at_index = MODULE.rl_39_split_at_index
rl_40_run_length_encode_recursive = MODULE.rl_40_run_length_encode_recursive
rl_41_total_length_nested = MODULE.rl_41_total_length_nested
rl_42_sum_nested_ints = MODULE.rl_42_sum_nested_ints
rl_43_flatten_nested = MODULE.rl_43_flatten_nested
rl_44_max_depth_nested = MODULE.rl_44_max_depth_nested
rl_45_contains_in_nested = MODULE.rl_45_contains_in_nested
rl_46_subsets_all = MODULE.rl_46_subsets_all
rl_47_permutations_all = MODULE.rl_47_permutations_all
rl_48_can_reach_sum_by_signs = MODULE.rl_48_can_reach_sum_by_signs
rl_49_split_into_two_equal_sum = MODULE.rl_49_split_into_two_equal_sum
rl_50_all_ways_to_split_into_runs = MODULE.rl_50_all_ways_to_split_into_runs


def test_basic_structural_recursion():
    assert rl_01_len_recursive([]) == 0
    assert rl_01_len_recursive([1, 2, 3]) == 3
    assert rl_02_sum_recursive([1, 2, 3]) == 6
    assert rl_03_count_occurrences([1, 2, 2, 3], 2) == 2
    assert rl_04_contains([1, 2, 3], 10) is False
    assert rl_05_all_positive([1, 2, 3]) is True
    assert rl_05_all_positive([1, -1]) is False
    assert rl_06_any_negative([1, -5, 2]) is True
    assert rl_06_any_negative([]) is False
    assert rl_07_max_recursive([3, 1, 4, 2]) == 4
    assert rl_07_max_recursive([]) is None
    assert rl_08_min_recursive([3, 1, 4, 2]) == 1
    assert rl_08_min_recursive([]) is None
    assert rl_09_index_of_first([5, 2, 5, 3], 5) == 0
    assert rl_09_index_of_first([1, 2, 3], 10) is None
    assert rl_10_index_of_last([5, 2, 5, 3], 5) == 2
    assert rl_10_index_of_last([1, 2, 3], 10) is None


def test_recursive_transformations():
    xs = [1, 2, 3]
    ys = rl_11_copy_list(xs)
    assert ys == xs and ys is not xs
    assert rl_12_reverse_new([1, 2, 3]) == [3, 2, 1]
    assert rl_13_increment_all([1, 2, 3], 5) == [6, 7, 8]
    assert rl_14_filter_even([1, 2, 3, 4, 5]) == [2, 4]
    assert rl_15_remove_target([1, 2, 2, 3], 2) == [1, 3]
    assert rl_16_take_first_n([1, 2, 3, 4], 2) == [1, 2]
    assert rl_17_drop_first_n([1, 2, 3, 4], 2) == [3, 4]
    assert rl_18_concat_lists([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert rl_19_interleave_recursive([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert rl_20_flatten_shallow([[1, 2], [], [3, 4]]) == [1, 2, 3, 4]


def test_divide_and_conquer_lists():
    assert rl_21_binary_search_recursive([1, 3, 5, 7], 5) is True
    assert rl_21_binary_search_recursive([1, 3, 5, 7], 6) is False
    assert rl_22_merge_two_sorted_recursive([1, 4, 6], [2, 3, 5]) == [1, 2, 3, 4, 5, 6]
    assert rl_23_merge_sort_recursive([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert rl_24_is_sorted_recursive([1, 2, 2, 3]) is True
    assert rl_24_is_sorted_recursive([3, 2, 1]) is False
    assert rl_25_count_inversions_simple([3, 1, 2]) == 2
    assert rl_26_count_smaller_to_right([3, 1, 2]) == [2, 0, 0]
    assert rl_27_max_subarray_sum_simple([1, -2, 3, 4]) == 7
    assert rl_27_max_subarray_sum_simple([-5, -2, -3]) == -2
    assert rl_27_max_subarray_sum_simple([]) is None
    assert rl_28_split_even_odd_indices([0, 1, 2, 3, 4]) == ([0, 2, 4], [1, 3])
    assert rl_28_split_even_odd_indices([]) == ([], [])
    assert rl_29_find_min_max_recursive([3, 1, 4, 2]) == (1, 4)
    assert rl_29_find_min_max_recursive([]) is None
    assert rl_30_rotate_left_recursive([1, 2, 3, 4], 1) == [2, 3, 4, 1]
    assert rl_30_rotate_left_recursive([], 5) == []


def test_two_sided_recursion_helpers():
    assert rl_31_len_from_index([1, 2, 3, 4], 1) == 3
    assert rl_31_len_from_index([1, 2], 2) == 0
    assert rl_32_sum_from_index([1, 2, 3, 4], 2) == 7
    assert rl_32_sum_from_index([1, 2], 5) == 0
    assert rl_33_is_palindrome_list([1, 2, 3, 2, 1]) is True
    assert rl_33_is_palindrome_list([1, 2, 3]) is False
    assert rl_34_lists_equal([1, 2, 3], [1, 2, 3]) is True
    assert rl_34_lists_equal([1, 2], [1, 2, 3]) is False
    assert rl_35_zip_lists_recursive([1, 2, 3], ["a", "b"]) == [(1, "a"), (2, "b")]
    assert rl_36_unzip_pairs_recursive([(1, "a"), (2, "b")]) == ([1, 2], ["a", "b"])
    assert rl_37_all_prefixes([1, 2, 3]) == [[], [1], [1, 2], [1, 2, 3]]
    assert rl_37_all_prefixes([]) == [[]]
    assert rl_38_all_suffixes([1, 2, 3]) == [[1, 2, 3], [2, 3], [3], []]
    assert rl_39_split_at_index([1, 2, 3, 4], 2) == ([1, 2], [3, 4])
    assert rl_39_split_at_index([1, 2], 10) == ([1, 2], [])
    assert rl_40_run_length_encode_recursive([1, 1, 2, 2, 2, 3]) == [(1, 2), (2, 3), (3, 1)]
    assert rl_40_run_length_encode_recursive([]) == []


def test_nested_structures():
    assert rl_41_total_length_nested([1, [2, 3], [], [4, [5]]]) == 5
    assert rl_42_sum_nested_ints([1, [2, 3], [4, [5]]]) == 15
    assert rl_43_flatten_nested([1, [2, [3, 4], []], 5]) == [1, 2, 3, 4, 5]
    assert rl_44_max_depth_nested([1, [2, [3]]]) == 3
    assert rl_44_max_depth_nested([]) == 1
    assert rl_45_contains_in_nested([1, [2, [3, 4]], 5], 4) is True
    assert rl_45_contains_in_nested([1, [2], []], 10) is False


def test_backtracking_combinatorial():
    subs = rl_46_subsets_all([1, 2])
    assert sorted(sorted(s) for s in subs) == [[], [1], [1, 2], [2]]
    perms = rl_47_permutations_all([1, 2])
    assert sorted(perms) == [[1, 2], [2, 1]]
    assert rl_47_permutations_all([]) == [[]]
    assert rl_48_can_reach_sum_by_signs([1, 2, 3], 0) is True
    assert rl_48_can_reach_sum_by_signs([2, 4], 1) is False
    assert rl_49_split_into_two_equal_sum([1, 5, 3, 3]) is True
    assert rl_49_split_into_two_equal_sum([1, 2, 3]) is True
    ways = rl_50_all_ways_to_split_into_runs([1, 2])
    assert sorted(sorted(run) for run in ways) == [[[1], [2]], [[1, 2]]]
