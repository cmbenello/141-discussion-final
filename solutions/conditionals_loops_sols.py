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
    if n >= 0:
        return sum(range(0, n + 1, 2))
    return sum(i for i in range(n, 1) if i % 2 == 0)

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
    if k == 0:
        raise ValueError("k must be non-zero")

    start, end = (a, b) if a <= b else (b, a)
    product = 1
    for num in range(start, end + 1):
        if num % k == 0:
            product *= num
    return product

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
    if k == 0:
        raise ValueError("k must be non-zero")

    return sum(1 for num in lst if num % k == 0)

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
    for idx, val in enumerate(lst):
        if val > x:
            return idx
    return None

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
    last_idx: Optional[int] = None
    for idx, val in enumerate(lst):
        if val < x:
            last_idx = idx
    return last_idx

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
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return True
    return False

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
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return i
    return None

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
    if not lst:
        return 0

    longest = 1
    current = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    return max(longest, current)

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
    if len(lst) < 2:
        return True

    for i in range(1, len(lst)):
        if lst[i] % 2 == lst[i - 1] % 2:
            return False
    return True

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
    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i - 1]) > max_step:
            return i
    return None

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
    left, right = 0, len(sorted_lst) - 1
    while left < right:
        total = sorted_lst[left] + sorted_lst[right]
        if total == target:
            return True
        if total < target:
            left += 1
        else:
            right -= 1
    return False

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
    if k <= 0 or k > len(lst):
        raise ValueError("k must be in the range 1..len(lst)")

    window_sum = sum(lst[:k])
    max_sum = window_sum

    for i in range(k, len(lst)):
        window_sum += lst[i] - lst[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum

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
    if n <= 0:
        raise ValueError("n must be positive")

    steps = 0
    current = n
    while current != 1 and steps < cap:
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
        steps += 1
    return steps

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
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a

    while b:
        a, b = b, a % b
    return a

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
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    base = x
    exponent = n
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result


def cl_16_sum_odd_indices(lst: List[int]) -> int:
    return sum(val for idx, val in enumerate(lst) if idx % 2 == 1)


def cl_17_count_negatives_until_positive(lst: List[int]) -> int:
    count = 0
    for val in lst:
        if val > 0:
            break
        if val < 0:
            count += 1
    return count


def cl_18_first_prefix_sum_gt(lst: List[int], threshold: int) -> Optional[int]:
    running = 0
    for idx, val in enumerate(lst):
        running += val
        if running > threshold:
            return idx
    return None


def cl_19_has_three_consecutive_increasing(lst: List[int]) -> bool:
    for i in range(len(lst) - 2):
        if lst[i] < lst[i + 1] < lst[i + 2]:
            return True
    return False


def cl_20_min_subarray_len_at_least(lst: List[int], target: int) -> Optional[int]:
    if target <= 0:
        return 0
    if not lst:
        return None

    min_len: Optional[int] = None
    window_sum = 0
    left = 0
    for right, val in enumerate(lst):
        window_sum += val
        while window_sum >= target and left <= right:
            current_len = right - left + 1
            min_len = current_len if min_len is None else min(min_len, current_len)
            window_sum -= lst[left]
            left += 1
    return min_len


def cl_21_count_runs(lst: List[int]) -> int:
    if not lst:
        return 0
    runs = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            runs += 1
    return runs


def cl_22_index_of_min_even(lst: List[int]) -> Optional[int]:
    best_idx: Optional[int] = None
    best_val: Optional[int] = None
    for idx, val in enumerate(lst):
        if val % 2 != 0:
            continue
        if best_val is None or val < best_val:
            best_val = val
            best_idx = idx
    return best_idx


def cl_23_sum_every_kth(lst: List[int], k: int) -> int:
    if k <= 0:
        raise ValueError("k must be positive")
    return sum(lst[i] for i in range(0, len(lst), k))


def cl_24_move_zeros_right(lst: List[int]) -> List[int]:
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros


def cl_25_is_palindrome_list(lst: List[int]) -> bool:
    return lst == lst[::-1]


def cl_26_running_maxima(lst: List[int]) -> List[int]:
    result: List[int] = []
    current_max: Optional[int] = None
    for val in lst:
        if current_max is None or val > current_max:
            current_max = val
        result.append(current_max)
    return result


def cl_27_count_pairs_with_diff_at_most(lst: List[int], d: int) -> int:
    if d < 0:
        raise ValueError("d must be non-negative")

    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if abs(lst[i] - lst[j]) <= d:
                count += 1
    return count


def cl_28_has_two_adjacent_sum(lst: List[int], target: int) -> bool:
    for i in range(len(lst) - 1):
        if lst[i] + lst[i + 1] == target:
            return True
    return False


def cl_29_chunk_and_sum(lst: List[int], size: int) -> List[int]:
    if size <= 0:
        raise ValueError("size must be positive")
    return [sum(lst[i : i + size]) for i in range(0, len(lst), size)]


def cl_30_count_valleys(steps: str) -> int:
    level = 0
    valleys = 0
    for step in steps:
        if step not in {"U", "D"}:
            raise ValueError("steps must contain only 'U' or 'D'")
        if step == "D":
            if level == 0:
                valleys += 1
            level -= 1
        else:
            level += 1
    return valleys
