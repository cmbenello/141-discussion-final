

"""
lists_tuples.py

Curated list/tuple-centric problems (exam/LeetCode style) organized with categories,
tags, and difficulty. These are meant to match CMSC 14100 final-level questions:
short, precise, and focused on core Python list/tuple skills.

Each function contains:
  - Category / Tags / Difficulty header in the docstring
  - Clear preconditions and examples
  - A stub implementation that raises ValueError("todo")

Students implement these in problems/lists_tuples.py.
Instructor solutions live in solutions/lists_tuples_sols.py and tests can switch
between them via USE_SOLUTIONS=1.
"""

from __future__ import annotations
from typing import List, Tuple, Optional, Any


# =====================================================================================
# Table of Contents
# =====================================================================================
# 1) Basic List/Tuple Mechanics
#    - lt_01_sum_list
#    - lt_02_average_list
#    - lt_03_max_index
#    - lt_04_find_all_indices
#    - lt_05_reverse_new
#    - lt_06_reverse_in_place
#
# 2) Ordering, Searching, and Insertion
#    - lt_07_is_sorted_non_decreasing
#    - lt_08_insert_sorted
#    - lt_09_remove_all
#    - lt_10_dedup_preserve_order
#
# 3) Pairwise Operations & Aggregations
#    - lt_11_pairwise_sums
#    - lt_12_dot_product
#    - lt_13_prefix_sums
#    - lt_14_windowed_sublists
#    - lt_15_chunk_list
#    - lt_16_zip_lists
#    - lt_17_unzip_pairs
#
# 4) Reordering & Interleaving
#    - lt_18_rotate_right
#    - lt_19_interleave_lists
#    - lt_20_partition_by_predicate
#
# 5) Nested Lists (Tables & Grids)
#    - lt_21_group_by_mod
#    - lt_22_flatten_list_of_lists
#    - lt_23_transpose_matrix
#    - lt_24_diagonal_sums
#
# 6) Statistics & Encodings
#    - lt_25_argmin_argmax
#    - lt_26_median_of_list
#    - lt_27_mode_of_list
#    - lt_28_run_length_encode_list
#    - lt_29_expand_run_length
#
# 7) Small Algorithmic Pattern
#    - lt_30_unique_pairs_sum_to
#
# Difficulty guide (approximate, 2–5):
#   2 = straightforward loop / indexing
#   3 = requires at least one non-trivial idea or careful edge handling
#   4 = multi-step reasoning or nested lists
#   5 = “challenge” problem at or above exam difficulty
# =====================================================================================


# =====================================================================================
# 1) Basic List/Tuple Mechanics
# =====================================================================================

def lt_01_sum_list(nums: List[int]) -> int:
    """
    Category: Basic List/Tuple Mechanics | Tags: accumulation, sum | Difficulty: 2

    Return the sum of all integers in nums. For an empty list, return 0.
    Do not use the built-in sum().

    Args:
        nums (List[int]): list of integers

    Returns:
        int: sum of all elements in nums

    Examples:
        >>> lt_01_sum_list([1, 2, 3])
        6
        >>> lt_01_sum_list([])
        0
    """
    raise ValueError("todo")


def lt_02_average_list(nums: List[float]) -> Optional[float]:
    """
    Category: Basic List/Tuple Mechanics | Tags: average, None-for-empty | Difficulty: 2

    Return the arithmetic mean (average) of the values in nums as a float.
    If nums is empty, return None.

    Args:
        nums (List[float]): list of numeric values

    Returns:
        Optional[float]: average of nums, or None if nums is empty

    Examples:
        >>> lt_02_average_list([1.0, 3.0, 5.0])
        3.0
        >>> lt_02_average_list([])
        None
    """
    raise ValueError("todo")


def lt_03_max_index(nums: List[int]) -> Optional[int]:
    """
    Category: Basic List/Tuple Mechanics | Tags: search, argmax | Difficulty: 3

    Return the index of the first maximum element in nums.
    If nums is empty, return None.

    Args:
        nums (List[int]): list of integers

    Returns:
        Optional[int]: index of the first occurrence of the maximum, or None if empty

    Examples:
        >>> lt_03_max_index([2, 7, 4, 7])
        1
        >>> lt_03_max_index([])
        None
    """
    raise ValueError("todo")


def lt_04_find_all_indices(nums: List[int], target: int) -> List[int]:
    """
    Category: Basic List/Tuple Mechanics | Tags: search, indices | Difficulty: 2

    Return a list of all indices i such that nums[i] == target.
    If target does not appear, return the empty list.

    Args:
        nums (List[int]): list of integers
        target (int): value to search for

    Returns:
        List[int]: list of indices where nums[i] == target

    Examples:
        >>> lt_04_find_all_indices([1, 3, 3, 2, 3], 3)
        [1, 2, 4]
        >>> lt_04_find_all_indices([1, 2, 3], 10)
        []
    """
    raise ValueError("todo")


def lt_05_reverse_new(seq: List[Any]) -> List[Any]:
    """
    Category: Basic List/Tuple Mechanics | Tags: reversal, copy | Difficulty: 2

    Return a NEW list that is the reverse of seq. Do not modify seq in place.
    Do not use list.reverse() or slicing with a negative step.

    Args:
        seq (List[Any]): list of any elements

    Returns:
        List[Any]: reversed copy of seq

    Examples:
        >>> lt_05_reverse_new([1, 2, 3])
        [3, 2, 1]
        >>> lt_05_reverse_new([])
        []
    """
    raise ValueError("todo")


def lt_06_reverse_in_place(seq: List[Any]) -> None:
    """
    Category: Basic List/Tuple Mechanics | Tags: reversal, in-place, two-pointer | Difficulty: 3

    Reverse the list seq IN PLACE and return None.
    You may not create a new list and copy back; instead, swap elements in seq.

    Args:
        seq (List[Any]): list to be reversed in place

    Returns:
        None

    Examples:
        >>> data = [1, 2, 3, 4]
        >>> lt_06_reverse_in_place(data)
        >>> data
        [4, 3, 2, 1]
    """
    raise ValueError("todo")


# =====================================================================================
# 2) Ordering, Searching, and Insertion
# =====================================================================================

def lt_07_is_sorted_non_decreasing(nums: List[int]) -> bool:
    """
    Category: Ordering & Searching | Tags: sorted, scan | Difficulty: 2

    Return True if nums is sorted in non-decreasing order (each element
    is >= the previous). Lists of length 0 or 1 are considered sorted.

    Args:
        nums (List[int]): list of integers

    Returns:
        bool: True if non-decreasing, else False

    Examples:
        >>> lt_07_is_sorted_non_decreasing([1, 2, 2, 3])
        True
        >>> lt_07_is_sorted_non_decreasing([3, 2, 1])
        False
    """
    raise ValueError("todo")


def lt_08_insert_sorted(nums: List[int], x: int) -> List[int]:
    """
    Category: Ordering & Searching | Tags: insertion, sorted, copy | Difficulty: 3

    Given a list nums that is already sorted in non-decreasing order,
    return a NEW list equal to nums with x inserted so that the result is
    still sorted. If there are existing copies of x, insert x after all
    smaller elements but before any larger ones (i.e., any position that
    keeps the list sorted is acceptable).

    Args:
        nums (List[int]): sorted list of integers
        x (int): value to insert

    Returns:
        List[int]: new sorted list with x inserted

    Examples:
        >>> lt_08_insert_sorted([1, 3, 5], 4)
        [1, 3, 4, 5]
        >>> lt_08_insert_sorted([], 10)
        [10]
    """
    raise ValueError("todo")


def lt_09_remove_all(seq: List[Any], target: Any) -> List[Any]:
    """
    Category: Ordering & Searching | Tags: filtering, removal | Difficulty: 2

    Return a NEW list equal to seq but with all elements equal to target removed.

    Args:
        seq (List[Any]): original list
        target (Any): value to remove

    Returns:
        List[Any]: new list with all target values removed

    Examples:
        >>> lt_09_remove_all([1, 2, 2, 3], 2)
        [1, 3]
        >>> lt_09_remove_all([], 0)
        []
    """
    raise ValueError("todo")


def lt_10_dedup_preserve_order(seq: List[Any]) -> List[Any]:
    """
    Category: Ordering & Searching | Tags: deduplication, stability | Difficulty: 3

    Return a NEW list where only the first occurrence of each distinct value
    from seq is kept, and later duplicates are removed. Preserve the original
    order of first occurrences.

    Args:
        seq (List[Any]): original list

    Returns:
        List[Any]: list with duplicates removed, order preserved

    Examples:
        >>> lt_10_dedup_preserve_order([3, 1, 3, 2, 1])
        [3, 1, 2]
        >>> lt_10_dedup_preserve_order([])
        []
    """
    raise ValueError("todo")


# =====================================================================================
# 3) Pairwise Operations & Aggregations
# =====================================================================================

def lt_11_pairwise_sums(a: List[int], b: List[int]) -> List[int]:
    """
    Category: Pairwise Operations | Tags: elementwise, zip-like | Difficulty: 2

    Given two lists a and b of the same length, return a new list where
    result[i] = a[i] + b[i] for all i.

    Args:
        a (List[int]): first list
        b (List[int]): second list, same length as a

    Returns:
        List[int]: elementwise sums

    Examples:
        >>> lt_11_pairwise_sums([1, 2, 3], [10, 20, 30])
        [11, 22, 33]
    """
    raise ValueError("todo")


def lt_12_dot_product(a: List[int], b: List[int]) -> int:
    """
    Category: Pairwise Operations | Tags: dot product, accumulation | Difficulty: 3

    Compute and return the dot product of a and b:
        sum_{i} a[i] * b[i]

    Precondition: len(a) == len(b).

    Args:
        a (List[int]): first list
        b (List[int]): second list

    Returns:
        int: dot product

    Examples:
        >>> lt_12_dot_product([1, 2, 3], [4, 5, 6])
        32
    """
    raise ValueError("todo")


def lt_13_prefix_sums(nums: List[int]) -> List[int]:
    """
    Category: Pairwise Operations | Tags: prefix sums, accumulation | Difficulty: 3

    Return a new list ps where ps[i] is the sum of nums[0] through nums[i].

    Args:
        nums (List[int]): list of integers

    Returns:
        List[int]: prefix sums

    Examples:
        >>> lt_13_prefix_sums([1, 2, 3, 4])
        [1, 3, 6, 10]
        >>> lt_13_prefix_sums([])
        []
    """
    raise ValueError("todo")


def lt_14_windowed_sublists(nums: List[int], k: int) -> List[List[int]]:
    """
    Category: Pairwise Operations | Tags: sliding window, sublists | Difficulty: 4

    Return all contiguous sublists (windows) of length k from nums, in order.
    If k <= 0 or k > len(nums), return [].

    Args:
        nums (List[int]): list of integers
        k (int): window length

    Returns:
        List[List[int]]: list of windows

    Examples:
        >>> lt_14_windowed_sublists([1, 2, 3, 4], 2)
        [[1, 2], [2, 3], [3, 4]]
        >>> lt_14_windowed_sublists([1, 2], 3)
        []
    """
    raise ValueError("todo")


def lt_15_chunk_list(seq: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Category: Pairwise Operations | Tags: chunking, grouping | Difficulty: 3

    Split seq into consecutive chunks (sublists) of size chunk_size.
    The final chunk may be shorter if len(seq) is not a multiple of chunk_size.
    If chunk_size <= 0, raise ValueError.

    Args:
        seq (List[Any]): original list
        chunk_size (int): positive chunk size

    Returns:
        List[List[Any]]: list of chunks

    Examples:
        >>> lt_15_chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    raise ValueError("todo")


def lt_16_zip_lists(a: List[Any], b: List[Any]) -> List[Tuple[Any, Any]]:
    """
    Category: Pairwise Operations | Tags: zip, tuples | Difficulty: 2

    Return a list of pairs (a[i], b[i]) for i from 0 up to min(len(a), len(b)) - 1.
    Similar to the built-in zip, but implemented with loops.

    Args:
        a (List[Any]): first list
        b (List[Any]): second list

    Returns:
        List[Tuple[Any, Any]]: list of pairs

    Examples:
        >>> lt_16_zip_lists([1, 2], ['a', 'b', 'c'])
        [(1, 'a'), (2, 'b')]
        >>> lt_16_zip_lists([], [1, 2])
        []
    """
    raise ValueError("todo")


def lt_17_unzip_pairs(pairs: List[Tuple[Any, Any]]) -> Tuple[List[Any], List[Any]]:
    """
    Category: Pairwise Operations | Tags: unzip, tuples | Difficulty: 2

    Given a list of pairs, return a tuple (xs, ys) where xs is a list of all
    first elements and ys is a list of all second elements.

    Args:
        pairs (List[Tuple[Any, Any]]): list of 2-tuples

    Returns:
        Tuple[List[Any], List[Any]]: (list_of_firsts, list_of_seconds)

    Examples:
        >>> lt_17_unzip_pairs([(1, 'a'), (2, 'b')])
        ([1], ['a'])  # doctest-style comparison ignores comment
    """
    raise ValueError("todo")


# =====================================================================================
# 4) Reordering & Interleaving
# =====================================================================================

def lt_18_rotate_right(nums: List[int], k: int) -> List[int]:
    """
    Category: Reordering & Interleaving | Tags: rotation, normalization | Difficulty: 3

    Return a NEW list equal to nums rotated right by k positions.
    For example, rotate_right([1,2,3,4], 1) -> [4,1,2,3].
    Normalize k so that it works for any (possibly large or negative) integer.

    Args:
        nums (List[int]): original list
        k (int): rotation amount

    Returns:
        List[int]: rotated list

    Examples:
        >>> lt_18_rotate_right([1, 2, 3, 4], 1)
        [4, 1, 2, 3]
        >>> lt_18_rotate_right([1, 2, 3, 4], 4)
        [1, 2, 3, 4]
        >>> lt_18_rotate_right([], 5)
        []
    """
    raise ValueError("todo")


def lt_19_interleave_lists(a: List[Any], b: List[Any]) -> List[Any]:
    """
    Category: Reordering & Interleaving | Tags: interleave, merge | Difficulty: 3

    Return a new list formed by interleaving elements from a and b:
    [a0, b0, a1, b1, ...] until one list runs out, then append the remaining
    elements from the longer list.

    Args:
        a (List[Any]): first list
        b (List[Any]): second list

    Returns:
        List[Any]: interleaved list

    Examples:
        >>> lt_19_interleave_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> lt_19_interleave_lists([1, 2], ['a', 'b', 'c'])
        [1, 'a', 2, 'b', 'c']
    """
    raise ValueError("todo")


def lt_20_partition_by_predicate(seq: List[int]) -> Tuple[List[int], List[int]]:
    """
    Category: Reordering & Interleaving | Tags: partition, predicate | Difficulty: 3

    Partition seq into evens and odds, returning (evens, odds) as NEW lists,
    each preserving the original relative order of its elements.

    Args:
        seq (List[int]): list of integers

    Returns:
        Tuple[List[int], List[int]]: (evens_in_order, odds_in_order)

    Examples:
        >>> lt_20_partition_by_predicate([5, 2, 4, 7, 6])
        ([2, 4, 6], [5, 7])
        >>> lt_20_partition_by_predicate([])
        ([], [])
    """
    raise ValueError("todo")


# =====================================================================================
# 5) Nested Lists (Tables & Grids)
# =====================================================================================

def lt_21_group_by_mod(nums: List[int], m: int) -> List[List[int]]:
    """
    Category: Nested Lists (Tables & Grids) | Tags: buckets, modulo | Difficulty: 4

    Group nums into m buckets by their remainder modulo m.
    Return a list of length m where result[r] is a list of all numbers x in nums
    such that x % m == r, in their original order.

    Precondition: m > 0.

    Args:
        nums (List[int]): list of integers
        m (int): positive modulus

    Returns:
        List[List[int]]: list of m buckets

    Examples:
        >>> lt_21_group_by_mod([0, 1, 2, 3, 4, 5], 3)
        [[0, 3], [1, 4], [2, 5]]
    """
    raise ValueError("todo")


def lt_22_flatten_list_of_lists(nested: List[List[Any]]) -> List[Any]:
    """
    Category: Nested Lists (Tables & Grids) | Tags: flattening | Difficulty: 2

    Given a list of lists, return a new flat list containing all elements in
    row-major order.

    Args:
        nested (List[List[Any]]): list of inner lists

    Returns:
        List[Any]: flattened list

    Examples:
        >>> lt_22_flatten_list_of_lists([[1, 2], [], [3]])
        [1, 2, 3]
        >>> lt_22_flatten_list_of_lists([])
        []
    """
    raise ValueError("todo")


def lt_23_transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Category: Nested Lists (Tables & Grids) | Tags: transpose, matrix | Difficulty: 4

    Given a rectangular matrix represented as a list of rows (all rows have the same
    length), return its transpose: rows become columns.

    Args:
        matrix (List[List[int]]): list of rows

    Returns:
        List[List[int]]: transposed matrix

    Examples:
        >>> lt_23_transpose_matrix([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
        >>> lt_23_transpose_matrix([])
        []
    """
    raise ValueError("todo")


def lt_24_diagonal_sums(square: List[List[int]]) -> Tuple[int, int]:
    """
    Category: Nested Lists (Tables & Grids) | Tags: diagonals, square matrix | Difficulty: 4

    Given an n-by-n square matrix of integers, return a tuple (main, anti) where:
      - main is the sum of the main diagonal (indices [0][0], [1][1], ..., [n-1][n-1])
      - anti is the sum of the anti-diagonal (indices [0][n-1], [1][n-2], ..., [n-1][0])

    Args:
        square (List[List[int]]): n-by-n matrix

    Returns:
        Tuple[int, int]: (main_diagonal_sum, anti_diagonal_sum)

    Examples:
        >>> lt_24_diagonal_sums([[1, 2], [3, 4]])
        (5, 5)
    """
    raise ValueError("todo")


# =====================================================================================
# 6) Statistics & Encodings
# =====================================================================================

def lt_25_argmin_argmax(nums: List[int]) -> Optional[Tuple[int, int]]:
    """
    Category: Statistics & Encodings | Tags: argmin, argmax | Difficulty: 3

    If nums is non-empty, return a pair (i_min, i_max) where:
      - i_min is the index of the first minimum value
      - i_max is the index of the first maximum value
    If nums is empty, return None.

    Args:
        nums (List[int]): list of integers

    Returns:
        Optional[Tuple[int, int]]: (index_of_min, index_of_max) or None

    Examples:
        >>> lt_25_argmin_argmax([3, 1, 4, 1, 5])
        (1, 4)
        >>> lt_25_argmin_argmax([])
        None
    """
    raise ValueError("todo")


def lt_26_median_of_list(nums: List[int]) -> Optional[float]:
    """
    Category: Statistics & Encodings | Tags: median, sorted copy | Difficulty: 4

    Return the median of nums as a float:
      - If len(nums) is odd, return the middle value of the sorted list.
      - If len(nums) is even, return the average of the two middle values.
      - If nums is empty, return None.

    You may make a sorted COPY of nums but must not mutate the original list.

    Args:
        nums (List[int]): list of integers

    Returns:
        Optional[float]: median value or None

    Examples:
        >>> lt_26_median_of_list([3, 1, 4])
        3.0
        >>> lt_26_median_of_list([1, 2, 3, 4])
        2.5
        >>> lt_26_median_of_list([])
        None
    """
    raise ValueError("todo")


def lt_27_mode_of_list(nums: List[int]) -> Optional[int]:
    """
    Category: Statistics & Encodings | Tags: frequency, mode | Difficulty: 4

    Return the mode (most frequent value) of nums.
    If nums is empty, return None. If there is a tie for highest frequency,
    return the smallest value among those tied elements.

    Args:
        nums (List[int]): list of integers

    Returns:
        Optional[int]: mode value or None

    Examples:
        >>> lt_27_mode_of_list([1, 2, 2, 3])
        2
        >>> lt_27_mode_of_list([3, 3, 1, 1])
        1
        >>> lt_27_mode_of_list([])
        None
    """
    raise ValueError("todo")


def lt_28_run_length_encode_list(seq: List[Any]) -> List[Tuple[Any, int]]:
    """
    Category: Statistics & Encodings | Tags: run length encoding, compression | Difficulty: 3

    Return the run-length encoding of seq as a list of (value, count) tuples.

    Args:
        seq (List[Any]): list of values

    Returns:
        List[Tuple[Any, int]]: run-length encoded representation

    Examples:
        >>> lt_28_run_length_encode_list([1, 1, 2, 2, 2, 3])
        [(1, 2), (2, 3), (3, 1)]
        >>> lt_28_run_length_encode_list([])
        []
    """
    raise ValueError("todo")


def lt_29_expand_run_length(encoded: List[Tuple[Any, int]]) -> List[Any]:
    """
    Category: Statistics & Encodings | Tags: run length decoding | Difficulty: 3

    Given a run-length encoded list of (value, count) tuples, return the
    expanded flat list where each value appears count times.

    Args:
        encoded (List[Tuple[Any, int]]): run-length encoding

    Returns:
        List[Any]: expanded list

    Examples:
        >>> lt_29_expand_run_length([('a', 3), ('b', 1)])
        ['a', 'a', 'a', 'b']
        >>> lt_29_expand_run_length([])
        []
    """
    raise ValueError("todo")


# =====================================================================================
# 7) Small Algorithmic Pattern
# =====================================================================================

def lt_30_unique_pairs_sum_to(nums: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Category: Small Algorithmic Pattern | Tags: pairs, sums, set-like behavior | Difficulty: 5

    Given a list of integers nums and an integer target, return a list of
    UNIQUE pairs (a, b) such that:
      - a + b == target
      - a and b are values taken from nums (indices may differ or be equal)
      - (a, b) is considered the same pair as (b, a), so include each unordered
        pair at most once.

    You may return the pairs in any order, but within each pair enforce a <= b.
    Use only lists/tuples and simple loops (no set or dict).

    Args:
        nums (List[int]): list of integers
        target (int): desired sum

    Returns:
        List[Tuple[int, int]]: list of unique pairs (a, b) with a + b == target

    Examples:
        >>> sorted(lt_30_unique_pairs_sum_to([1, 2, 3, 4, 5], 6))
        [(1, 5), (2, 4)]
        >>> lt_30_unique_pairs_sum_to([3, 3, 3], 6)
        [(3, 3)]
        >>> lt_30_unique_pairs_sum_to([], 0)
        []
    """
    raise ValueError("todo")