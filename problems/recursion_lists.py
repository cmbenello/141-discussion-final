

"""
recursion_lists.py

Curated recursion-on-lists problem set (exam/LeetCode style) organized with categories,
tags, and difficulty. These are meant to match CMSC 14100 final-level questions, with
an emphasis on *structural recursion* over Python lists and tuples.

Each function contains:
  - Category / Tags / Difficulty header in the docstring
  - Clear preconditions and examples
  - A stub implementation that raises ValueError("todo")

Students implement these in problems/recursion_lists.py.
Instructor solutions live in solutions/recursion_lists_sols.py and tests can switch
between them via USE_SOLUTIONS=1.
"""

from __future__ import annotations
from typing import List, Tuple, Optional, Any


# =====================================================================================
# Table of Contents
# =====================================================================================
# 1) Basic Structural Recursion on Flat Lists
#    - rl_01_len_recursive
#    - rl_02_sum_recursive
#    - rl_03_count_occurrences
#    - rl_04_contains
#    - rl_05_all_positive
#    - rl_06_any_negative
#    - rl_07_max_recursive
#    - rl_08_min_recursive
#    - rl_09_index_of_first
#    - rl_10_index_of_last
#
# 2) Recursive List Transformations (Map/Filter/Build)
#    - rl_11_copy_list
#    - rl_12_reverse_new
#    - rl_13_increment_all
#    - rl_14_filter_even
#    - rl_15_remove_target
#    - rl_16_take_first_n
#    - rl_17_drop_first_n
#    - rl_18_concat_lists
#    - rl_19_interleave_recursive
#    - rl_20_flatten_shallow
#
# 3) Divide-and-Conquer on Lists
#    - rl_21_binary_search_recursive
#    - rl_22_merge_two_sorted_recursive
#    - rl_23_merge_sort_recursive
#    - rl_24_is_sorted_recursive
#    - rl_25_count_inversions_simple
#    - rl_26_count_smaller_to_right
#    - rl_27_max_subarray_sum_simple
#    - rl_28_split_even_odd_indices
#    - rl_29_find_min_max_recursive
#    - rl_30_rotate_left_recursive
#
# 4) Recursive Algorithms with Indices / Two-Sided Recursion
#    - rl_31_len_from_index
#    - rl_32_sum_from_index
#    - rl_33_is_palindrome_list
#    - rl_34_lists_equal
#    - rl_35_zip_lists_recursive
#    - rl_36_unzip_pairs_recursive
#    - rl_37_all_prefixes
#    - rl_38_all_suffixes
#    - rl_39_split_at_index
#    - rl_40_run_length_encode_recursive
#
# 5) Nested Lists and Simple Tree-Like Structures
#    - rl_41_total_length_nested
#    - rl_42_sum_nested_ints
#    - rl_43_flatten_nested
#    - rl_44_max_depth_nested
#    - rl_45_contains_in_nested
#
# 6) Backtracking / Combinatorial Recursion (List-Focused)
#    - rl_46_subsets_all
#    - rl_47_permutations_all
#    - rl_48_can_reach_sum_by_signs
#    - rl_49_split_into_two_equal_sum
#    - rl_50_all_ways_to_split_into_runs
#
# Difficulty guide (approximate, 2–5):
#   2 = straightforward structural recursion with simple base case
#   3 = needs at least one non-trivial idea or careful combination step
#   4 = multi-step reasoning, indices, or nested lists
#   5 = “challenge” backtracking or divide-and-conquer style
# =====================================================================================


# =====================================================================================
# 1) Basic Structural Recursion on Flat Lists
# =====================================================================================

def rl_01_len_recursive(xs: List[Any]) -> int:
    """
    Category: Basic Structural Recursion | Tags: length, base_case, recursion | Difficulty: 2

    Recursively compute the length of the list xs without using len().

    Args:
        xs (List[Any]): list of any elements

    Returns:
        int: number of elements in xs

    Examples:
        >>> rl_01_len_recursive([])
        0
        >>> rl_01_len_recursive([1, 2, 3])
        3
    """
    raise ValueError("todo")


def rl_02_sum_recursive(xs: List[int]) -> int:
    """
    Category: Basic Structural Recursion | Tags: sum, integers | Difficulty: 2

    Recursively compute the sum of all integers in xs.
    For an empty list, return 0.

    Args:
        xs (List[int]): list of integers

    Returns:
        int: sum of all elements

    Examples:
        >>> rl_02_sum_recursive([])
        0
        >>> rl_02_sum_recursive([1, 2, 3])
        6
    """
    raise ValueError("todo")


def rl_03_count_occurrences(xs: List[Any], target: Any) -> int:
    """
    Category: Basic Structural Recursion | Tags: count, equality | Difficulty: 2

    Recursively count how many times target appears in xs.

    Args:
        xs (List[Any]): list of elements
        target (Any): value to count

    Returns:
        int: number of occurrences of target

    Examples:
        >>> rl_03_count_occurrences([1, 2, 2, 3], 2)
        2
        >>> rl_03_count_occurrences([], 5)
        0
    """
    raise ValueError("todo")


def rl_04_contains(xs: List[Any], target: Any) -> bool:
    """
    Category: Basic Structural Recursion | Tags: search, membership | Difficulty: 2

    Recursively determine whether target appears in xs.

    Args:
        xs (List[Any]): list of elements
        target (Any): value to search for

    Returns:
        bool: True if target in xs, else False

    Examples:
        >>> rl_04_contains([1, 2, 3], 2)
        True
        >>> rl_04_contains([1, 2, 3], 10)
        False
    """
    raise ValueError("todo")


def rl_05_all_positive(xs: List[int]) -> bool:
    """
    Category: Basic Structural Recursion | Tags: all, predicate | Difficulty: 2

    Recursively check whether all integers in xs are strictly > 0.
    The empty list is considered to satisfy the condition (vacuously True).

    Args:
        xs (List[int]): list of integers

    Returns:
        bool: True if all x > 0, else False

    Examples:
        >>> rl_05_all_positive([1, 2, 3])
        True
        >>> rl_05_all_positive([1, -1, 2])
        False
        >>> rl_05_all_positive([])
        True
    """
    raise ValueError("todo")


def rl_06_any_negative(xs: List[int]) -> bool:
    """
    Category: Basic Structural Recursion | Tags: any, predicate | Difficulty: 2

    Recursively check whether any integer in xs is < 0.

    Args:
        xs (List[int]): list of integers

    Returns:
        bool: True if some x < 0, else False

    Examples:
        >>> rl_06_any_negative([1, 2, 3])
        False
        >>> rl_06_any_negative([1, -5, 2])
        True
        >>> rl_06_any_negative([])
        False
    """
    raise ValueError("todo")


def rl_07_max_recursive(xs: List[int]) -> Optional[int]:
    """
    Category: Basic Structural Recursion | Tags: max, non-empty, option | Difficulty: 3

    Recursively compute the maximum value in xs.
    If xs is empty, return None instead of raising an error.

    Args:
        xs (List[int]): list of integers

    Returns:
        Optional[int]: maximum value or None if xs is empty

    Examples:
        >>> rl_07_max_recursive([3, 1, 4, 2])
        4
        >>> rl_07_max_recursive([])
        None
    """
    raise ValueError("todo")


def rl_08_min_recursive(xs: List[int]) -> Optional[int]:
    """
    Category: Basic Structural Recursion | Tags: min, non-empty, option | Difficulty: 3

    Recursively compute the minimum value in xs.
    If xs is empty, return None.

    Args:
        xs (List[int]): list of integers

    Returns:
        Optional[int]: minimum value or None

    Examples:
        >>> rl_08_min_recursive([3, 1, 4, 2])
        1
        >>> rl_08_min_recursive([])
        None
    """
    raise ValueError("todo")


def rl_09_index_of_first(xs: List[Any], target: Any) -> Optional[int]:
    """
    Category: Basic Structural Recursion | Tags: search, index | Difficulty: 3

    Recursively find the index of the first occurrence of target in xs.
    If target does not appear, return None.

    Args:
        xs (List[Any]): list of elements
        target (Any): value to search for

    Returns:
        Optional[int]: index of first occurrence, or None

    Examples:
        >>> rl_09_index_of_first([5, 2, 5, 3], 5)
        0
        >>> rl_09_index_of_first([1, 2, 3], 10)
        None
    """
    raise ValueError("todo")


def rl_10_index_of_last(xs: List[Any], target: Any) -> Optional[int]:
    """
    Category: Basic Structural Recursion | Tags: search, index, from-end | Difficulty: 3

    Recursively find the index of the last occurrence of target in xs.
    If target does not appear, return None.

    Args:
        xs (List[Any]): list of elements
        target (Any): value to search for

    Returns:
        Optional[int]: index of last occurrence, or None

    Examples:
        >>> rl_10_index_of_last([5, 2, 5, 3], 5)
        2
        >>> rl_10_index_of_last([1, 2, 3], 10)
        None
    """
    raise ValueError("todo")


# =====================================================================================
# 2) Recursive List Transformations (Map/Filter/Build)
# =====================================================================================

def rl_11_copy_list(xs: List[Any]) -> List[Any]:
    """
    Category: Recursive Transformations | Tags: copy, clone | Difficulty: 2

    Recursively produce a NEW list equal to xs. Do not use slicing or list().

    Args:
        xs (List[Any]): list to copy

    Returns:
        List[Any]: new list with the same elements

    Examples:
        >>> xs = [1, 2, 3]
        >>> ys = rl_11_copy_list(xs)
        >>> ys
        [1, 2, 3]
        >>> xs is ys
        False
    """
    raise ValueError("todo")


def rl_12_reverse_new(xs: List[Any]) -> List[Any]:
    """
    Category: Recursive Transformations | Tags: reverse, build_new | Difficulty: 3

    Recursively build and return a NEW list that is the reverse of xs.
    Do not call list.reverse() or slicing with a negative step.

    Args:
        xs (List[Any]): original list

    Returns:
        List[Any]: reversed copy

    Examples:
        >>> rl_12_reverse_new([1, 2, 3])
        [3, 2, 1]
        >>> rl_12_reverse_new([])
        []
    """
    raise ValueError("todo")


def rl_13_increment_all(xs: List[int], k: int) -> List[int]:
    """
    Category: Recursive Transformations | Tags: map, arithmetic | Difficulty: 2

    Recursively return a NEW list where each element is x + k for x in xs.

    Args:
        xs (List[int]): list of integers
        k (int): amount to add

    Returns:
        List[int]: incremented list

    Examples:
        >>> rl_13_increment_all([1, 2, 3], 5)
        [6, 7, 8]
    """
    raise ValueError("todo")


def rl_14_filter_even(xs: List[int]) -> List[int]:
    """
    Category: Recursive Transformations | Tags: filter, parity | Difficulty: 3

    Recursively return a NEW list containing only the even numbers from xs,
    in their original order.

    Args:
        xs (List[int]): list of integers

    Returns:
        List[int]: evens from xs

    Examples:
        >>> rl_14_filter_even([1, 2, 3, 4, 5])
        [2, 4]
        >>> rl_14_filter_even([])
        []
    """
    raise ValueError("todo")


def rl_15_remove_target(xs: List[Any], target: Any) -> List[Any]:
    """
    Category: Recursive Transformations | Tags: filter, removal | Difficulty: 3

    Recursively return a NEW list equal to xs but with all elements equal
    to target removed.

    Args:
        xs (List[Any]): original list
        target (Any): value to remove

    Returns:
        List[Any]: list without any occurrences of target

    Examples:
        >>> rl_15_remove_target([1, 2, 2, 3], 2)
        [1, 3]
        >>> rl_15_remove_target([], 0)
        []
    """
    raise ValueError("todo")


def rl_16_take_first_n(xs: List[Any], n: int) -> List[Any]:
    """
    Category: Recursive Transformations | Tags: prefix, slicing | Difficulty: 3

    Recursively return a NEW list containing the first n elements of xs.
    If n <= 0, return []. If n >= len(xs), return a copy of xs.

    Args:
        xs (List[Any]): original list
        n (int): number of elements to take

    Returns:
        List[Any]: first n elements

    Examples:
        >>> rl_16_take_first_n([1, 2, 3, 4], 2)
        [1, 2]
        >>> rl_16_take_first_n([1, 2], 10)
        [1, 2]
        >>> rl_16_take_first_n([1, 2], 0)
        []
    """
    raise ValueError("todo")


def rl_17_drop_first_n(xs: List[Any], n: int) -> List[Any]:
    """
    Category: Recursive Transformations | Tags: suffix, slicing | Difficulty: 3

    Recursively return a NEW list equal to xs but with the first n elements
    removed. If n <= 0, return a copy of xs. If n >= len(xs), return [].

    Args:
        xs (List[Any]): original list
        n (int): number of elements to drop

    Returns:
        List[Any]: list without the first n elements

    Examples:
        >>> rl_17_drop_first_n([1, 2, 3, 4], 2)
        [3, 4]
        >>> rl_17_drop_first_n([1, 2], 10)
        []
    """
    raise ValueError("todo")


def rl_18_concat_lists(a: List[Any], b: List[Any]) -> List[Any]:
    """
    Category: Recursive Transformations | Tags: concatenation, build | Difficulty: 2

    Recursively build and return a NEW list equal to a + b (concatenation)
    without using the + operator on lists.

    Args:
        a (List[Any]): first list
        b (List[Any]): second list

    Returns:
        List[Any]: concatenation of a and b

    Examples:
        >>> rl_18_concat_lists([1, 2], [3, 4])
        [1, 2, 3, 4]
        >>> rl_18_concat_lists([], [1])
        [1]
    """
    raise ValueError("todo")


def rl_19_interleave_recursive(a: List[Any], b: List[Any]) -> List[Any]:
    """
    Category: Recursive Transformations | Tags: interleave, merge | Difficulty: 4

    Recursively interleave lists a and b into a single list:
    [a0, b0, a1, b1, ...] until one list runs out, then append the remaining
    elements from the longer list.

    Args:
        a (List[Any]): first list
        b (List[Any]): second list

    Returns:
        List[Any]: interleaved list

    Examples:
        >>> rl_19_interleave_recursive([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> rl_19_interleave_recursive([1, 2], ['a'])
        [1, 'a', 2]
    """
    raise ValueError("todo")


def rl_20_flatten_shallow(nested: List[List[Any]]) -> List[Any]:
    """
    Category: Recursive Transformations | Tags: flatten, shallow | Difficulty: 3

    Recursively flatten a *shallow* list of lists nested (one level only).
    That is, each element of nested is itself a list, and you should return
    a single flat list of their elements in order.

    Args:
        nested (List[List[Any]]): list of inner lists

    Returns:
        List[Any]: flattened list

    Examples:
        >>> rl_20_flatten_shallow([[1, 2], [], [3, 4]])
        [1, 2, 3, 4]
        >>> rl_20_flatten_shallow([])
        []
    """
    raise ValueError("todo")


# =====================================================================================
# 3) Divide-and-Conquer on Lists
# =====================================================================================

def rl_21_binary_search_recursive(sorted_xs: List[int], target: int) -> bool:
    """
    Category: Divide-and-Conquer | Tags: binary search, sorted | Difficulty: 3

    Recursively perform binary search on a sorted list of integers sorted_xs
    to determine whether target is present.

    Args:
        sorted_xs (List[int]): list sorted in non-decreasing order
        target (int): value to search for

    Returns:
        bool: True if target appears in sorted_xs, else False

    Examples:
        >>> rl_21_binary_search_recursive([1, 3, 5, 7], 5)
        True
        >>> rl_21_binary_search_recursive([1, 3, 5, 7], 6)
        False
    """
    raise ValueError("todo")


def rl_22_merge_two_sorted_recursive(a: List[int], b: List[int]) -> List[int]:
    """
    Category: Divide-and-Conquer | Tags: merge, sorted lists | Difficulty: 3

    Recursively merge two sorted lists a and b (non-decreasing order) into a
    single sorted list.

    Args:
        a (List[int]): first sorted list
        b (List[int]): second sorted list

    Returns:
        List[int]: merged sorted list

    Examples:
        >>> rl_22_merge_two_sorted_recursive([1, 4, 6], [2, 3, 5])
        [1, 2, 3, 4, 5, 6]
        >>> rl_22_merge_two_sorted_recursive([], [1, 2])
        [1, 2]
    """
    raise ValueError("todo")


def rl_23_merge_sort_recursive(xs: List[int]) -> List[int]:
    """
    Category: Divide-and-Conquer | Tags: merge sort, recursion | Difficulty: 4

    Recursively sort xs using merge sort and return a NEW sorted list.
    You may use rl_22_merge_two_sorted_recursive as a helper.

    Args:
        xs (List[int]): list of integers

    Returns:
        List[int]: sorted copy of xs

    Examples:
        >>> rl_23_merge_sort_recursive([3, 1, 4, 1, 5])
        [1, 1, 3, 4, 5]
        >>> rl_23_merge_sort_recursive([])
        []
    """
    raise ValueError("todo")


def rl_24_is_sorted_recursive(xs: List[int]) -> bool:
    """
    Category: Divide-and-Conquer | Tags: sorted, adjacency | Difficulty: 3

    Recursively check whether xs is sorted in non-decreasing order.

    Args:
        xs (List[int]): list of integers

    Returns:
        bool: True if sorted, else False

    Examples:
        >>> rl_24_is_sorted_recursive([1, 2, 2, 3])
        True
        >>> rl_24_is_sorted_recursive([3, 2, 1])
        False
    """
    raise ValueError("todo")


def rl_25_count_inversions_simple(xs: List[int]) -> int:
    """
    Category: Divide-and-Conquer | Tags: inversions, pairs | Difficulty: 4

    An inversion is a pair of indices (i, j) with i < j and xs[i] > xs[j].
    Recursively count the number of inversions in xs.
    A simple O(n^2) approach with recursion is fine here (no need for
    advanced divide-and-conquer optimization).

    Args:
        xs (List[int]): list of integers

    Returns:
        int: number of inversions

    Examples:
        >>> rl_25_count_inversions_simple([3, 1, 2])
        2   # (3,1), (3,2)
        >>> rl_25_count_inversions_simple([1, 2, 3])
        0
    """
    raise ValueError("todo")


def rl_26_count_smaller_to_right(xs: List[int]) -> List[int]:
    """
    Category: Divide-and-Conquer | Tags: counts, suffix | Difficulty: 4

    For each index i, count how many elements xs[j] with j > i satisfy
    xs[j] < xs[i]. Return a list of these counts of the same length as xs.

    A straightforward recursive definition is fine (not optimized).

    Args:
        xs (List[int]): list of integers

    Returns:
        List[int]: counts of smaller elements to the right

    Examples:
        >>> rl_26_count_smaller_to_right([3, 1, 2])
        [2, 0, 0]
        >>> rl_26_count_smaller_to_right([])
        []
    """
    raise ValueError("todo")


def rl_27_max_subarray_sum_simple(xs: List[int]) -> Optional[int]:
    """
    Category: Divide-and-Conquer | Tags: subarray, recursion | Difficulty: 4

    Return the maximum sum of any *non-empty* contiguous subarray of xs.
    Use a simple recursive approach (not Kadane's optimized algorithm).
    If xs is empty, return None.

    Args:
        xs (List[int]): list of integers

    Returns:
        Optional[int]: maximum subarray sum or None

    Examples:
        >>> rl_27_max_subarray_sum_simple([1, -2, 3, 4])
        7
        >>> rl_27_max_subarray_sum_simple([-5, -2, -3])
        -2
        >>> rl_27_max_subarray_sum_simple([])
        None
    """
    raise ValueError("todo")


def rl_28_split_even_odd_indices(xs: List[Any]) -> Tuple[List[Any], List[Any]]:
    """
    Category: Divide-and-Conquer | Tags: split, indices | Difficulty: 3

    Recursively split xs into elements at even indices and elements at odd
    indices, returning a pair (evens, odds). Indexing is 0-based, so xs[0]
    is considered even index.

    Args:
        xs (List[Any]): original list

    Returns:
        Tuple[List[Any], List[Any]]: (elements_at_even_indices, elements_at_odd_indices)

    Examples:
        >>> rl_28_split_even_odd_indices([0, 1, 2, 3, 4])
        ([0, 2, 4], [1, 3])
        >>> rl_28_split_even_odd_indices([])
        ([], [])
    """
    raise ValueError("todo")


def rl_29_find_min_max_recursive(xs: List[int]) -> Optional[Tuple[int, int]]:
    """
    Category: Divide-and-Conquer | Tags: min, max, pair | Difficulty: 3

    Recursively compute both the minimum and maximum of xs, returning
    a tuple (min_value, max_value). If xs is empty, return None.

    Args:
        xs (List[int]): list of integers

    Returns:
        Optional[Tuple[int, int]]: (min_value, max_value) or None

    Examples:
        >>> rl_29_find_min_max_recursive([3, 1, 4, 2])
        (1, 4)
        >>> rl_29_find_min_max_recursive([])
        None
    """
    raise ValueError("todo")


def rl_30_rotate_left_recursive(xs: List[Any], k: int) -> List[Any]:
    """
    Category: Divide-and-Conquer | Tags: rotation, normalize | Difficulty: 3

    Recursively return a NEW list equal to xs rotated left by k positions.
    Normalize k so that it works for any integer (possibly negative or larger
    than len(xs)).

    Args:
        xs (List[Any]): original list
        k (int): number of positions to rotate left

    Returns:
        List[Any]: rotated list

    Examples:
        >>> rl_30_rotate_left_recursive([1, 2, 3, 4], 1)
        [2, 3, 4, 1]
        >>> rl_30_rotate_left_recursive([1, 2, 3, 4], 4)
        [1, 2, 3, 4]
        >>> rl_30_rotate_left_recursive([], 5)
        []
    """
    raise ValueError("todo")


# =====================================================================================
# 4) Recursive Algorithms with Indices / Two-Sided Recursion
# =====================================================================================

def rl_31_len_from_index(xs: List[Any], i: int) -> int:
    """
    Category: Indices / Two-Sided Recursion | Tags: helper, index | Difficulty: 3

    Recursively compute the length of xs starting from index i.
    If i is already past the end of xs, return 0.

    Args:
        xs (List[Any]): list of elements
        i (int): starting index (0-based)

    Returns:
        int: number of elements from i to end

    Examples:
        >>> rl_31_len_from_index([1, 2, 3, 4], 1)
        3
        >>> rl_31_len_from_index([1, 2], 2)
        0
    """
    raise ValueError("todo")


def rl_32_sum_from_index(xs: List[int], i: int) -> int:
    """
    Category: Indices / Two-Sided Recursion | Tags: helper, index | Difficulty: 3

    Recursively compute the sum of xs[i:] (from index i to the end).
    If i is already past the end of xs, return 0.

    Args:
        xs (List[int]): list of integers
        i (int): starting index

    Returns:
        int: sum of xs[i:]

    Examples:
        >>> rl_32_sum_from_index([1, 2, 3, 4], 2)
        7
        >>> rl_32_sum_from_index([1, 2], 5)
        0
    """
    raise ValueError("todo")


def rl_33_is_palindrome_list(xs: List[Any]) -> bool:
    """
    Category: Indices / Two-Sided Recursion | Tags: palindrome, front/back | Difficulty: 4

    Recursively determine whether xs reads the same forwards and backwards.

    Args:
        xs (List[Any]): list of elements

    Returns:
        bool: True if palindrome, else False

    Examples:
        >>> rl_33_is_palindrome_list([1, 2, 3, 2, 1])
        True
        >>> rl_33_is_palindrome_list([1, 2, 3])
        False
        >>> rl_33_is_palindrome_list([])
        True
    """
    raise ValueError("todo")


def rl_34_lists_equal(a: List[Any], b: List[Any]) -> bool:
    """
    Category: Indices / Two-Sided Recursion | Tags: equality, pairwise | Difficulty: 3

    Recursively check whether two lists a and b are equal: same length and
    same elements in the same order.

    Args:
        a (List[Any]): first list
        b (List[Any]): second list

    Returns:
        bool: True if a and b are equal, else False

    Examples:
        >>> rl_34_lists_equal([1, 2, 3], [1, 2, 3])
        True
        >>> rl_34_lists_equal([1, 2], [1, 2, 3])
        False
    """
    raise ValueError("todo")


def rl_35_zip_lists_recursive(a: List[Any], b: List[Any]) -> List[Tuple[Any, Any]]:
    """
    Category: Indices / Two-Sided Recursion | Tags: zip, tuples | Difficulty: 3

    Recursively combine two lists a and b into a list of pairs (a[i], b[i])
    up to the length of the shorter list.

    Args:
        a (List[Any]): first list
        b (List[Any]): second list

    Returns:
        List[Tuple[Any, Any]]: list of pairs

    Examples:
        >>> rl_35_zip_lists_recursive([1, 2, 3], ['a', 'b'])
        [(1, 'a'), (2, 'b')]
        >>> rl_35_zip_lists_recursive([], [1, 2])
        []
    """
    raise ValueError("todo")


def rl_36_unzip_pairs_recursive(pairs: List[Tuple[Any, Any]]) -> Tuple[List[Any], List[Any]]:
    """
    Category: Indices / Two-Sided Recursion | Tags: unzip, tuples | Difficulty: 3

    Recursively "unzip" a list of pairs into a pair of lists: (firsts, seconds).

    Args:
        pairs (List[Tuple[Any, Any]]): list of 2-tuples

    Returns:
        Tuple[List[Any], List[Any]]: (list_of_firsts, list_of_seconds)

    Examples:
        >>> rl_36_unzip_pairs_recursive([(1, 'a'), (2, 'b')])
        ([1, 2], ['a', 'b'])
        >>> rl_36_unzip_pairs_recursive([])
        ([], [])
    """
    raise ValueError("todo")


def rl_37_all_prefixes(xs: List[Any]) -> List[List[Any]]:
    """
    Category: Indices / Two-Sided Recursion | Tags: prefixes, building | Difficulty: 4

    Recursively generate all prefixes of xs, from the empty prefix up to xs
    itself, in order of increasing length.

    Args:
        xs (List[Any]): original list

    Returns:
        List[List[Any]]: list of prefixes

    Examples:
        >>> rl_37_all_prefixes([1, 2, 3])
        [[], [1], [1, 2], [1, 2, 3]]
        >>> rl_37_all_prefixes([])
        [[]]
    """
    raise ValueError("todo")


def rl_38_all_suffixes(xs: List[Any]) -> List[List[Any]]:
    """
    Category: Indices / Two-Sided Recursion | Tags: suffixes, building | Difficulty: 4

    Recursively generate all suffixes of xs, from xs itself down to the
    empty suffix, in order of decreasing length.

    Args:
        xs (List[Any]): original list

    Returns:
        List[List[Any]]: list of suffixes

    Examples:
        >>> rl_38_all_suffixes([1, 2, 3])
        [[1, 2, 3], [2, 3], [3], []]
        >>> rl_38_all_suffixes([])
        [[]]
    """
    raise ValueError("todo")


def rl_39_split_at_index(xs: List[Any], k: int) -> Tuple[List[Any], List[Any]]:
    """
    Category: Indices / Two-Sided Recursion | Tags: split, index | Difficulty: 3

    Recursively split xs into (prefix, suffix) at index k such that:
      - prefix contains the first k elements (or all of xs if k >= len(xs))
      - suffix contains the remaining elements (or [] if k >= len(xs))
    For k <= 0, prefix should be [], suffix should be a copy of xs.

    Args:
        xs (List[Any]): original list
        k (int): split index

    Returns:
        Tuple[List[Any], List[Any]]: (prefix, suffix)

    Examples:
        >>> rl_39_split_at_index([1, 2, 3, 4], 2)
        ([1, 2], [3, 4])
        >>> rl_39_split_at_index([1, 2], 10)
        ([1, 2], [])
    """
    raise ValueError("todo")


def rl_40_run_length_encode_recursive(xs: List[Any]) -> List[Tuple[Any, int]]:
    """
    Category: Indices / Two-Sided Recursion | Tags: run-length encoding | Difficulty: 4

    Recursively compute the run-length encoding of xs as a list of
    (value, count) tuples.

    Args:
        xs (List[Any]): list of values

    Returns:
        List[Tuple[Any, int]]: run-length encoded list

    Examples:
        >>> rl_40_run_length_encode_recursive([1, 1, 2, 2, 2, 3])
        [(1, 2), (2, 3), (3, 1)]
        >>> rl_40_run_length_encode_recursive([])
        []
    """
    raise ValueError("todo")


# =====================================================================================
# 5) Nested Lists and Simple Tree-Like Structures
# =====================================================================================

def rl_41_total_length_nested(nested: List[Any]) -> int:
    """
    Category: Nested Lists | Tags: total length, nested | Difficulty: 4

    Given a nested list structure where each element is either:
      - a non-list value, or
      - another nested list,
    recursively compute the total number of non-list elements inside.

    Args:
        nested (List[Any]): nested list structure

    Returns:
        int: total count of non-list elements

    Examples:
        >>> rl_41_total_length_nested([1, [2, 3], [], [4, [5]]])
        5
        >>> rl_41_total_length_nested([])
        0
    """
    raise ValueError("todo")


def rl_42_sum_nested_ints(nested: List[Any]) -> int:
    """
    Category: Nested Lists | Tags: sum, nested ints | Difficulty: 4

    Given a nested list structure where non-list elements are integers,
    recursively compute the sum of all integers.

    Args:
        nested (List[Any]): nested list of ints and/or sublists

    Returns:
        int: sum of all integer elements

    Examples:
        >>> rl_42_sum_nested_ints([1, [2, 3], [4, [5]]])
        15
        >>> rl_42_sum_nested_ints([])
        0
    """
    raise ValueError("todo")


def rl_43_flatten_nested(nested: List[Any]) -> List[Any]:
    """
    Category: Nested Lists | Tags: flatten, arbitrary depth | Difficulty: 4

    Recursively flatten a nested list structure of arbitrary depth into
    a single flat list of all non-list elements in left-to-right order.

    Args:
        nested (List[Any]): nested list structure

    Returns:
        List[Any]: flattened list

    Examples:
        >>> rl_43_flatten_nested([1, [2, [3, 4], []], 5])
        [1, 2, 3, 4, 5]
        >>> rl_43_flatten_nested([])
        []
    """
    raise ValueError("todo")


def rl_44_max_depth_nested(nested: List[Any]) -> int:
    """
    Category: Nested Lists | Tags: depth, nesting | Difficulty: 4

    Recursively compute the maximum nesting depth of nested. The empty list
    has depth 1 (one level). Each additional list inside increases depth.

    Args:
        nested (List[Any]): nested list structure

    Returns:
        int: maximum depth

    Examples:
        >>> rl_44_max_depth_nested([1, 2, 3])
        1
        >>> rl_44_max_depth_nested([1, [2, [3]]])
        3
        >>> rl_44_max_depth_nested([])
        1
    """
    raise ValueError("todo")


def rl_45_contains_in_nested(nested: List[Any], target: Any) -> bool:
    """
    Category: Nested Lists | Tags: search, nested | Difficulty: 3

    Recursively check whether target appears anywhere inside the nested list
    structure (at any depth).

    Args:
        nested (List[Any]): nested list structure
        target (Any): value to search for

    Returns:
        bool: True if target appears, else False

    Examples:
        >>> rl_45_contains_in_nested([1, [2, [3, 4]], 5], 4)
        True
        >>> rl_45_contains_in_nested([1, [2], []], 10)
        False
    """
    raise ValueError("todo")


# =====================================================================================
# 6) Backtracking / Combinatorial Recursion (List-Focused)
# =====================================================================================

def rl_46_subsets_all(xs: List[Any]) -> List[List[Any]]:
    """
    Category: Backtracking / Combinatorial | Tags: subsets, powerset | Difficulty: 5

    Recursively generate the power set (set of all subsets) of xs as a list
    of lists. The order of subsets and elements within a subset does not
    matter for correctness, but each subset should use the elements of xs
    in their original relative order.

    Args:
        xs (List[Any]): original list

    Returns:
        List[List[Any]]: list of all subsets

    Examples:
        >>> sorted([sorted(sub) for sub in rl_46_subsets_all([1, 2])])
        [[], [1], [1, 2], [2]]
    """
    raise ValueError("todo")


def rl_47_permutations_all(xs: List[Any]) -> List[List[Any]]:
    """
    Category: Backtracking / Combinatorial | Tags: permutations | Difficulty: 5

    Recursively generate all permutations of the list xs.
    Each permutation is itself represented as a list.

    Args:
        xs (List[Any]): original list (no duplicate elements assumed)

    Returns:
        List[List[Any]]: list of permutations

    Examples:
        >>> sorted(rl_47_permutations_all([1, 2]))
        [[1, 2], [2, 1]]
        >>> rl_47_permutations_all([])
        [[]]
    """
    raise ValueError("todo")


def rl_48_can_reach_sum_by_signs(xs: List[int], target: int) -> bool:
    """
    Category: Backtracking / Combinatorial | Tags: +/- signs, target sum | Difficulty: 5

    Given a list xs of integers, recursively decide whether it is possible to
    assign each element either a '+' or '-' sign so that the resulting sum
    equals target.

    For example, with xs = [1, 2, 3] and target = 0, we can choose
    1 - 2 + 3 = 2 (not 0), but -1 - 2 + 3 = 0, so the answer is True.

    Args:
        xs (List[int]): list of integers
        target (int): desired sum

    Returns:
        bool: True if some assignment of signs yields target, else False

    Examples:
        >>> rl_48_can_reach_sum_by_signs([1, 2, 3], 0)
        True
        >>> rl_48_can_reach_sum_by_signs([2, 4], 1)
        False
    """
    raise ValueError("todo")


def rl_49_split_into_two_equal_sum(xs: List[int]) -> bool:
    """
    Category: Backtracking / Combinatorial | Tags: partition, equal sum | Difficulty: 5

    Recursively determine whether xs can be partitioned into two (possibly
    empty) groups of elements that have the same total sum. Each element must
    belong to exactly one of the two groups.

    Args:
        xs (List[int]): list of integers

    Returns:
        bool: True if such a partition exists, else False

    Examples:
        >>> rl_49_split_into_two_equal_sum([1, 5, 3, 3])
        True   # e.g., [1,5] and [3,3]
        >>> rl_49_split_into_two_equal_sum([1, 2, 3])
        False
    """
    raise ValueError("todo")


def rl_50_all_ways_to_split_into_runs(xs: List[Any]) -> List[List[List[Any]]]:
    """
    Category: Backtracking / Combinatorial | Tags: segmentation, runs | Difficulty: 5

    Recursively generate all ways to split xs into contiguous runs (segments).
    Each "way" is represented as a list of segments, where each segment is a
    non-empty sublist of xs, and concatenating all segments in order gives xs.

    For example, for xs = [1, 2, 3], some valid splittings are:
      - [[1, 2, 3]]
      - [[1], [2, 3]]
      - [[1, 2], [3]]
      - [[1], [2], [3]]

    Args:
        xs (List[Any]): original list

    Returns:
        List[List[List[Any]]]: list of all segmentations

    Examples:
        >>> segs = rl_50_all_ways_to_split_into_runs([1, 2])
        >>> sorted(sorted(run) for run in segs)  # doctest won't care about exact order
        [[[1], [2]], [[1, 2]]]
    """
    raise ValueError("todo")