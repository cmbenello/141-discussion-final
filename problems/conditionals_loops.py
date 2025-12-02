from __future__ import annotations
from typing import List, Optional


def cl_01_sum_even_up_to(n: int) -> int:
    """
    Category: Conditionals/Loops
    Difficulty: Easy
    Args:
        n (int): The integer up to which to sum even numbers.
    Returns:
        int: The sum of even numbers from 0 up to n (inclusive) if n >= 0,
             or from n up to 0 (inclusive) if n < 0.
    Examples:
        >>> cl_01_sum_even_up_to(6)
        12
        >>> cl_01_sum_even_up_to(-4)
        -6
    """
    raise ValueError("todo")


def cl_02_product_multiples_range(a: int, b: int, k: int) -> int:
    """
    Category: Conditionals/Loops
    Difficulty: Easy
    Args:
        a (int): Start of the range.
        b (int): End of the range.
        k (int): Multiple factor.
    Returns:
        int: Product of all numbers between a and b inclusive that are multiples of k.
             Returns 1 if no such numbers exist.
    Examples:
        >>> cl_02_product_multiples_range(1, 10, 3)
        18
        >>> cl_02_product_multiples_range(5, 7, 10)
        1
    """
    raise ValueError("todo")


def cl_03_count_divisible(lst: List[int], k: int) -> int:
    """
    Category: Conditionals/Loops
    Difficulty: Easy
    Args:
        lst (List[int]): List of integers.
        k (int): Divisor.
    Returns:
        int: Count of elements in lst divisible by k.
    Examples:
        >>> cl_03_count_divisible([2,3,4,6,9], 3)
        3
        >>> cl_03_count_divisible([], 1)
        0
    """
    raise ValueError("todo")


def cl_04_first_index_gt(lst: List[int], x: int) -> Optional[int]:
    """
    Category: Conditionals/Loops
    Difficulty: Easy
    Args:
        lst (List[int]): List of integers.
        x (int): Threshold value.
    Returns:
        Optional[int]: Index of first element greater than x, or None if none found.
    Examples:
        >>> cl_04_first_index_gt([1,2,3,4], 2)
        2
        >>> cl_04_first_index_gt([1,2,3], 5) is None
        True
    """
    raise ValueError("todo")


def cl_05_last_index_lt(lst: List[int], x: int) -> Optional[int]:
    """
    Category: Conditionals/Loops
    Difficulty: Easy
    Args:
        lst (List[int]): List of integers.
        x (int): Threshold value.
    Returns:
        Optional[int]: Last index of element less than x, or None if none found.
    Examples:
        >>> cl_05_last_index_lt([1,4,2,5], 3)
        2
        >>> cl_05_last_index_lt([5,6,7], 4) is None
        True
    """
    raise ValueError("todo")


def cl_06_has_adjacent_equal(lst: List[int]) -> bool:
    """
    Category: Conditionals/Loops
    Difficulty: Easy
    Args:
        lst (List[int]): List of integers.
    Returns:
        bool: True if any adjacent elements are equal, False otherwise.
    Examples:
        >>> cl_06_has_adjacent_equal([1,2,2,3])
        True
        >>> cl_06_has_adjacent_equal([1,2,3])
        False
    """
    raise ValueError("todo")


def cl_07_first_strict_increase_pair(lst: List[int]) -> Optional[int]:
    """
    Category: Conditionals/Loops
    Difficulty: Easy
    Args:
        lst (List[int]): List of integers.
    Returns:
        Optional[int]: Index of first element where lst[i] < lst[i+1], or None if none.
    Examples:
        >>> cl_07_first_strict_increase_pair([3,2,4,1])
        1
        >>> cl_07_first_strict_increase_pair([5,4,3])
        None
    """
    raise ValueError("todo")


def cl_08_longest_run_equal(lst: List[int]) -> int:
    """
    Category: Conditionals/Loops
    Difficulty: Medium
    Args:
        lst (List[int]): List of integers.
    Returns:
        int: Length of longest run of equal adjacent elements.
    Examples:
        >>> cl_08_longest_run_equal([1,1,2,2,2,3])
        3
        >>> cl_08_longest_run_equal([])
        0
    """
    raise ValueError("todo")


def cl_09_is_alternating_parity(lst: List[int]) -> bool:
    """
    Category: Conditionals/Loops
    Difficulty: Medium
    Args:
        lst (List[int]): List of integers.
    Returns:
        bool: True if elements alternate parity (even/odd), False otherwise.
    Examples:
        >>> cl_09_is_alternating_parity([1,2,3,4])
        True
        >>> cl_09_is_alternating_parity([2,4,6])
        False
    """
    raise ValueError("todo")


def cl_10_first_violation_max_step(lst: List[int], max_step: int) -> Optional[int]:
    """
    Category: Conditionals/Loops
    Difficulty: Medium
    Args:
        lst (List[int]): List of integers.
        max_step (int): Maximum allowed step difference.
    Returns:
        Optional[int]: First index i where abs(lst[i] - lst[i-1]) > max_step, or None.
    Examples:
        >>> cl_10_first_violation_max_step([1,3,7,8], 3)
        2
        >>> cl_10_first_violation_max_step([1,2,3], 5) is None
        True
    """
    raise ValueError("todo")


def cl_11_two_sum_exists(sorted_lst: List[int], target: int) -> bool:
    """
    Category: Conditionals/Loops
    Difficulty: Medium
    Args:
        sorted_lst (List[int]): Sorted list of integers.
        target (int): Target sum.
    Returns:
        bool: True if any two numbers sum to target, False otherwise.
    Examples:
        >>> cl_11_two_sum_exists([1,2,3,4], 5)
        True
        >>> cl_11_two_sum_exists([1,2,3], 7)
        False
    """
    raise ValueError("todo")


def cl_12_sliding_window_max_sum(lst: List[int], k: int) -> int:
    """
    Category: Conditionals/Loops
    Difficulty: Medium
    Args:
        lst (List[int]): List of integers.
        k (int): Window size.
    Returns:
        int: Maximum sum of any contiguous subarray of length k.
    Raises:
        ValueError: If k <= 0 or k > len(lst).
    Examples:
        >>> cl_12_sliding_window_max_sum([1,2,3,4], 2)
        7
        >>> cl_12_sliding_window_max_sum([1,2,3], 3)
        6
    """
    raise ValueError("todo")


def cl_13_collatz_steps(n: int, cap: int) -> int:
    """
    Category: Conditionals/Loops
    Difficulty: Medium
    Args:
        n (int): Starting number.
        cap (int): Maximum steps to simulate.
    Returns:
        int: Number of steps to reach 1 or cap if 1 not reached.
    Examples:
        >>> cl_13_collatz_steps(6, 10)
        8
        >>> cl_13_collatz_steps(1, 5)
        0
    """
    raise ValueError("todo")


def cl_14_gcd_euclid(a: int, b: int) -> int:
    """
    Category: Conditionals/Loops
    Difficulty: Medium
    Args:
        a (int): First integer.
        b (int): Second integer.
    Returns:
        int: Greatest common divisor of a and b.
    Examples:
        >>> cl_14_gcd_euclid(24, 18)
        6
        >>> cl_14_gcd_euclid(-12, 30)
        6
    """
    raise ValueError("todo")


def cl_15_pow_int(x: int, n: int) -> int:
    """
    Category: Conditionals/Loops
    Difficulty: Medium
    Args:
        x (int): Base integer.
        n (int): Non-negative exponent.
    Returns:
        int: x raised to the power n.
    Examples:
        >>> cl_15_pow_int(2, 3)
        8
        >>> cl_15_pow_int(5, 0)
        1
    """
    raise ValueError("todo")


def cl_16_sum_odd_indices(lst: List[int]) -> int:
    raise ValueError("todo")


def cl_17_count_negatives_until_positive(lst: List[int]) -> int:
    raise ValueError("todo")


def cl_18_first_prefix_sum_gt(lst: List[int], threshold: int) -> Optional[int]:
    raise ValueError("todo")


def cl_19_has_three_consecutive_increasing(lst: List[int]) -> bool:
    raise ValueError("todo")


def cl_20_min_subarray_len_at_least(lst: List[int], target: int) -> Optional[int]:
    raise ValueError("todo")


def cl_21_count_runs(lst: List[int]) -> int:
    raise ValueError("todo")


def cl_22_index_of_min_even(lst: List[int]) -> Optional[int]:
    raise ValueError("todo")


def cl_23_sum_every_kth(lst: List[int], k: int) -> int:
    raise ValueError("todo")


def cl_24_move_zeros_right(lst: List[int]) -> List[int]:
    raise ValueError("todo")


def cl_25_is_palindrome_list(lst: List[int]) -> bool:
    raise ValueError("todo")


def cl_26_running_maxima(lst: List[int]) -> List[int]:
    raise ValueError("todo")


def cl_27_count_pairs_with_diff_at_most(lst: List[int], d: int) -> int:
    raise ValueError("todo")


def cl_28_has_two_adjacent_sum(lst: List[int], target: int) -> bool:
    raise ValueError("todo")


def cl_29_chunk_and_sum(lst: List[int], size: int) -> List[int]:
    raise ValueError("todo")


def cl_30_count_valleys(steps: str) -> int:
    raise ValueError("todo")
