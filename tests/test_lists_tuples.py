from __future__ import annotations

import importlib
import os

import pytest


USE_SOLUTIONS = os.getenv("USE_SOLUTIONS") == "1"
MODULE = importlib.import_module(
    "solutions.lists_tuples_sols" if USE_SOLUTIONS else "problems.lists_tuples"
)

lt_01_sum_list = MODULE.lt_01_sum_list
lt_02_average_list = MODULE.lt_02_average_list
lt_03_max_index = MODULE.lt_03_max_index
lt_04_find_all_indices = MODULE.lt_04_find_all_indices
lt_05_reverse_new = MODULE.lt_05_reverse_new
lt_06_reverse_in_place = MODULE.lt_06_reverse_in_place
lt_07_is_sorted_non_decreasing = MODULE.lt_07_is_sorted_non_decreasing
lt_08_insert_sorted = MODULE.lt_08_insert_sorted
lt_09_remove_all = MODULE.lt_09_remove_all
lt_10_dedup_preserve_order = MODULE.lt_10_dedup_preserve_order
lt_11_pairwise_sums = MODULE.lt_11_pairwise_sums
lt_12_dot_product = MODULE.lt_12_dot_product
lt_13_prefix_sums = MODULE.lt_13_prefix_sums
lt_14_windowed_sublists = MODULE.lt_14_windowed_sublists
lt_15_chunk_list = MODULE.lt_15_chunk_list
lt_16_zip_lists = MODULE.lt_16_zip_lists
lt_17_unzip_pairs = MODULE.lt_17_unzip_pairs
lt_18_rotate_right = MODULE.lt_18_rotate_right
lt_19_interleave_lists = MODULE.lt_19_interleave_lists
lt_20_partition_by_predicate = MODULE.lt_20_partition_by_predicate
lt_21_group_by_mod = MODULE.lt_21_group_by_mod
lt_22_flatten_list_of_lists = MODULE.lt_22_flatten_list_of_lists
lt_23_transpose_matrix = MODULE.lt_23_transpose_matrix
lt_24_diagonal_sums = MODULE.lt_24_diagonal_sums
lt_25_argmin_argmax = MODULE.lt_25_argmin_argmax
lt_26_median_of_list = MODULE.lt_26_median_of_list
lt_27_mode_of_list = MODULE.lt_27_mode_of_list
lt_28_run_length_encode_list = MODULE.lt_28_run_length_encode_list
lt_29_expand_run_length = MODULE.lt_29_expand_run_length
lt_30_unique_pairs_sum_to = MODULE.lt_30_unique_pairs_sum_to


def test_lt_01_sum_list_basic():
    assert lt_01_sum_list([1, 2, 3]) == 6
    assert lt_01_sum_list([]) == 0


def test_lt_02_average_list_none_and_value():
    assert lt_02_average_list([]) is None
    assert lt_02_average_list([2.0, 4.0]) == 3.0


def test_lt_03_max_index_first_occurrence():
    assert lt_03_max_index([2, 7, 4, 7]) == 1
    assert lt_03_max_index([]) is None


def test_lt_04_find_all_indices_matches():
    assert lt_04_find_all_indices([1, 3, 3, 2, 3], 3) == [1, 2, 4]
    assert lt_04_find_all_indices([1, 2, 3], 10) == []


def test_lt_05_reverse_new_and_no_mutation():
    src = [1, 2, 3]
    assert lt_05_reverse_new(src) == [3, 2, 1]
    assert src == [1, 2, 3]


def test_lt_06_reverse_in_place_mutates():
    data = [1, 2, 3, 4]
    lt_06_reverse_in_place(data)
    assert data == [4, 3, 2, 1]


def test_lt_07_is_sorted_non_decreasing_cases():
    assert lt_07_is_sorted_non_decreasing([1, 2, 2, 3]) is True
    assert lt_07_is_sorted_non_decreasing([3, 2, 1]) is False
    assert lt_07_is_sorted_non_decreasing([]) is True


def test_lt_08_insert_sorted_positions():
    assert lt_08_insert_sorted([1, 3, 5], 4) == [1, 3, 4, 5]
    assert lt_08_insert_sorted([], 10) == [10]
    assert lt_08_insert_sorted([1, 2, 4], 0) == [0, 1, 2, 4]


def test_lt_09_remove_all_filters():
    assert lt_09_remove_all([1, 2, 2, 3], 2) == [1, 3]
    assert lt_09_remove_all([], 0) == []


def test_lt_10_dedup_preserve_order_keeps_firsts():
    assert lt_10_dedup_preserve_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert lt_10_dedup_preserve_order([]) == []


def test_lt_11_pairwise_sums():
    assert lt_11_pairwise_sums([1, 2, 3], [10, 20, 30]) == [11, 22, 33]


def test_lt_12_dot_product():
    assert lt_12_dot_product([1, 2, 3], [4, 5, 6]) == 32


def test_lt_13_prefix_sums_handles_empty():
    assert lt_13_prefix_sums([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert lt_13_prefix_sums([]) == []


def test_lt_14_windowed_sublists_valid_and_invalid():
    assert lt_14_windowed_sublists([1, 2, 3, 4], 2) == [[1, 2], [2, 3], [3, 4]]
    assert lt_14_windowed_sublists([1, 2], 3) == []
    assert lt_14_windowed_sublists([1, 2], 0) == []


def test_lt_15_chunk_list_chunks_and_errors():
    assert lt_15_chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    with pytest.raises(ValueError):
        lt_15_chunk_list([1, 2], 0)


def test_lt_16_zip_lists_shorter_second():
    assert lt_16_zip_lists([1, 2], ["a", "b", "c"]) == [(1, "a"), (2, "b")]
    assert lt_16_zip_lists([], [1, 2]) == []


def test_lt_17_unzip_pairs_round_trip():
    pairs = [(1, "a"), (2, "b")]
    assert lt_17_unzip_pairs(pairs) == ([1, 2], ["a", "b"])


def test_lt_18_rotate_right_wraps_and_negative():
    assert lt_18_rotate_right([1, 2, 3, 4], 1) == [4, 1, 2, 3]
    assert lt_18_rotate_right([1, 2, 3, 4], 4) == [1, 2, 3, 4]
    assert lt_18_rotate_right([1, 2, 3], -1) == [2, 3, 1]
    assert lt_18_rotate_right([], 5) == []


def test_lt_19_interleave_lists_varied_lengths():
    assert lt_19_interleave_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert lt_19_interleave_lists([1, 2], ["a", "b", "c"]) == [1, "a", 2, "b", "c"]


def test_lt_20_partition_by_predicate_evens_odds():
    assert lt_20_partition_by_predicate([5, 2, 4, 7, 6]) == ([2, 4, 6], [5, 7])
    assert lt_20_partition_by_predicate([]) == ([], [])


def test_lt_21_group_by_mod_buckets_and_error():
    assert lt_21_group_by_mod([0, 1, 2, 3, 4, 5], 3) == [[0, 3], [1, 4], [2, 5]]
    with pytest.raises(ValueError):
        lt_21_group_by_mod([1, 2], 0)


def test_lt_22_flatten_list_of_lists_handles_empty():
    assert lt_22_flatten_list_of_lists([[1, 2], [], [3]]) == [1, 2, 3]
    assert lt_22_flatten_list_of_lists([]) == []


def test_lt_23_transpose_matrix_rectangular_and_empty():
    assert lt_23_transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert lt_23_transpose_matrix([]) == []


def test_lt_24_diagonal_sums_square():
    assert lt_24_diagonal_sums([[1, 2], [3, 4]]) == (5, 5)
    assert lt_24_diagonal_sums([[5]]) == (5, 5)


def test_lt_25_argmin_argmax_results():
    assert lt_25_argmin_argmax([3, 1, 4, 1, 5]) == (1, 4)
    assert lt_25_argmin_argmax([]) is None


def test_lt_26_median_of_list_even_odd_and_empty():
    assert lt_26_median_of_list([3, 1, 4]) == 3.0
    assert lt_26_median_of_list([1, 2, 3, 4]) == 2.5
    assert lt_26_median_of_list([]) is None


def test_lt_27_mode_of_list_tie_break_smallest():
    assert lt_27_mode_of_list([1, 2, 2, 3]) == 2
    assert lt_27_mode_of_list([3, 3, 1, 1]) == 1
    assert lt_27_mode_of_list([]) is None


def test_lt_28_run_length_encode_list_handles_runs():
    assert lt_28_run_length_encode_list([1, 1, 2, 2, 2, 3]) == [(1, 2), (2, 3), (3, 1)]
    assert lt_28_run_length_encode_list([]) == []


def test_lt_29_expand_run_length_decodes():
    assert lt_29_expand_run_length([("a", 3), ("b", 1)]) == ["a", "a", "a", "b"]
    assert lt_29_expand_run_length([]) == []


def test_lt_30_unique_pairs_sum_to_unique_unordered():
    pairs = lt_30_unique_pairs_sum_to([1, 2, 3, 4, 5], 6)
    assert sorted(pairs) == [(1, 5), (2, 4), (3, 3)]
    assert lt_30_unique_pairs_sum_to([3, 3, 3], 6) == [(3, 3)]
    assert lt_30_unique_pairs_sum_to([], 0) == []
