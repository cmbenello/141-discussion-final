"""
basics.py

Combined problem set for:
  - Basic expressions, types, and small utilities
  - Lists & tuples (including mutation vs. copying)
  - Functions, arguments, and scoping / mutability
  - Simple classes & objects

Target difficulty: CMSC 14100 exam-style levels 2–5.

Each function/method includes:
  - Category / Tags / Difficulty
  - Clear specification
  - Doctest-style examples where helpful
  - Stub implementation that raises ValueError("todo")

Students implement these in problems/basics.py.
Instructor solutions live in solutions/basics_sols.py.
Tests swap between stubs and solutions via USE_SOLUTIONS=1.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Dict


# =====================================================================================
# TABLE OF CONTENTS
# =====================================================================================
#
# 1) Expressions & Basic Types Utilities
#    - ba_01_add_three
#    - ba_02_safe_int_div
#    - ba_03_average_ignore_none
#    - ba_04_clamp
#    - ba_05_quadratic_eval
#    - ba_06_is_close
#    - ba_07_to_bool_list
#    - ba_08_parse_rgb_hex
#    - ba_09_seconds_to_hms
#    - ba_10_hms_to_seconds
#
# 2) Lists & Tuples (Structure, Mutation, Derived Data)
#    - ba_11_first_last
#    - ba_12_rotate_right
#    - ba_13_remove_negatives_in_place
#    - ba_14_dedup_preserve_order
#    - ba_15_pairwise_sums
#    - ba_16_split_by_parity
#    - ba_17_chunk_list
#    - ba_18_argmax
#    - ba_19_all_prefix_sums
#    - ba_20_interleave_lists
#
# 3) Functions, Arguments & Mutability / Scope
#    - ba_21_increment_all_in_place
#    - ba_22_increment_copy
#    - ba_23_append_log
#    - ba_24_copy_and_append
#    - ba_25_update_counter
#    - ba_26_clone_and_update_counter
#    - ba_27_safe_pop
#    - ba_28_zero_out_below_threshold
#    - ba_29_extend_if_short
#    - ba_30_normalize_scores
#
# 4) Classes & Objects (Simple Data Models)
#    - Point2D
#         - translate
#         - scaled
#         - distance_to
#         - __str__
#    - BankAccount
#         - deposit
#         - withdraw
#         - transfer_to
#         - apply_interest
#    - TodoList
#         - add_task
#         - complete_task
#         - pending_tasks
#         - __len__
#
# =====================================================================================


# =====================================================================================
# 1) EXPRESSIONS & BASIC TYPES UTILITIES
# =====================================================================================

def ba_01_add_three(a: int, b: int, c: int) -> int:
    """
    Category: Basics | Tags: arithmetic, expressions | Difficulty: 2

    Return the sum of three integers.

    Args:
        a, b, c (int): integers to add

    Returns:
        int: a + b + c

    Examples:
        >>> ba_01_add_three(1, 2, 3)
        6
        >>> ba_01_add_three(-5, 0, 2)
        -3
    """
    raise ValueError("todo")


def ba_02_safe_int_div(n: int, d: int) -> Optional[int]:
    """
    Category: Basics | Tags: integer division, None | Difficulty: 2

    Perform integer division n // d. If d == 0, return None instead of raising.

    Args:
        n (int): numerator
        d (int): denominator

    Returns:
        Optional[int]: n // d if d != 0, else None

    Examples:
        >>> ba_02_safe_int_div(7, 2)
        3
        >>> ba_02_safe_int_div(5, 0) is None
        True
    """
    raise ValueError("todo")


def ba_03_average_ignore_none(values: List[Optional[float]]) -> Optional[float]:
    """
    Category: Basics | Tags: average, None, filtering | Difficulty: 3

    Compute the arithmetic mean of all non-None values in the list.
    If there are no non-None values, return None.

    Args:
        values (List[Optional[float]]): list of numbers or None placeholders

    Returns:
        Optional[float]: mean of non-None values, or None if none

    Examples:
        >>> ba_03_average_ignore_none([1.0, None, 3.0])
        2.0
        >>> ba_03_average_ignore_none([None, None]) is None
        True
    """
    raise ValueError("todo")


def ba_04_clamp(x: int, lo: int, hi: int) -> int:
    """
    Category: Basics | Tags: conditionals, min_max | Difficulty: 2

    Clamp x into the inclusive range [lo, hi].

    - If x < lo, return lo.
    - If x > hi, return hi.
    - Otherwise, return x.

    Precondition: lo <= hi.

    Examples:
        >>> ba_04_clamp(5, 0, 10)
        5
        >>> ba_04_clamp(-3, 0, 10)
        0
        >>> ba_04_clamp(99, 0, 10)
        10
    """
    raise ValueError("todo")


def ba_05_quadratic_eval(a: float, b: float, c: float, x: float) -> float:
    """
    Category: Basics | Tags: expressions, numeric | Difficulty: 2

    Evaluate the quadratic polynomial a*x^2 + b*x + c at x.

    Examples:
        >>> ba_05_quadratic_eval(1.0, 0.0, 0.0, 2.0)
        4.0
        >>> ba_05_quadratic_eval(1.0, -1.0, 0.0, 1.0)
        0.0
    """
    raise ValueError("todo")


def ba_06_is_close(a: float, b: float, eps: float = 1e-6) -> bool:
    """
    Category: Basics | Tags: floating point, comparison | Difficulty: 3

    Return True iff |a - b| <= eps.

    Args:
        a, b (float): numbers to compare
        eps (float): tolerance (non-negative)

    Examples:
        >>> ba_06_is_close(1.0, 1.0000001)
        True
        >>> ba_06_is_close(1.0, 1.1)
        False
    """
    raise ValueError("todo")


def ba_07_to_bool_list(bits: str) -> List[int]:
    """
    Category: Basics | Tags: strings, lists, conversion | Difficulty: 3

    Given a string of '0' and '1' characters, return a list of integers 0/1.

    If any other character appears, raise ValueError.

    Examples:
        >>> ba_07_to_bool_list("1010")
        [1, 0, 1, 0]
        >>> ba_07_to_bool_list("")
        []
    """
    raise ValueError("todo")


def ba_08_parse_rgb_hex(code: str) -> Tuple[int, int, int]:
    """
    Category: Basics | Tags: strings, numeric parsing | Difficulty: 4

    Parse a color in '#RRGGBB' hex format and return (r, g, b) as integers 0–255.

    Requirements:
      - code must start with '#'
      - followed by exactly 6 hex digits (0–9, a–f, A–F)
      - raise ValueError if the format is invalid

    Examples:
        >>> ba_08_parse_rgb_hex("#000000")
        (0, 0, 0)
        >>> ba_08_parse_rgb_hex("#FF00ff")
        (255, 0, 255)
    """
    raise ValueError("todo")


def ba_09_seconds_to_hms(total: int) -> Tuple[int, int, int]:
    """
    Category: Basics | Tags: integer arithmetic, time | Difficulty: 3

    Convert a non-negative number of seconds to (hours, minutes, seconds).

    Assumptions:
        - total >= 0

    Examples:
        >>> ba_09_seconds_to_hms(0)
        (0, 0, 0)
        >>> ba_09_seconds_to_hms(3661)
        (1, 1, 1)
    """
    raise ValueError("todo")


def ba_10_hms_to_seconds(h: int, m: int, s: int) -> int:
    """
    Category: Basics | Tags: integer arithmetic, time | Difficulty: 3

    Convert hours, minutes, seconds into total seconds.
    Assume all inputs are non-negative and m, s are in [0, 59].

    Examples:
        >>> ba_10_hms_to_seconds(0, 0, 0)
        0
        >>> ba_10_hms_to_seconds(1, 1, 1)
        3661
    """
    raise ValueError("todo")


# =====================================================================================
# 2) LISTS & TUPLES (STRUCTURE, MUTATION, DERIVED DATA)
# =====================================================================================

def ba_11_first_last(lst: List[int]) -> Optional[Tuple[int, int]]:
    """
    Category: Lists & Tuples | Tags: indexing, option | Difficulty: 2

    If lst is non-empty, return a (first, last) tuple of its elements.
    If lst is empty, return None.

    Examples:
        >>> ba_11_first_last([10])
        (10, 10)
        >>> ba_11_first_last([]) is None
        True
        >>> ba_11_first_last([1, 2, 3])
        (1, 3)
    """
    raise ValueError("todo")


def ba_12_rotate_right(lst: List[int], k: int) -> List[int]:
    """
    Category: Lists & Tuples | Tags: rotation, index arithmetic | Difficulty: 3

    Return a NEW list that is lst rotated right by k positions.
    Normalize k by len(lst). For an empty list, always return [].

    Examples:
        >>> ba_12_rotate_right([1, 2, 3, 4], 1)
        [4, 1, 2, 3]
        >>> ba_12_rotate_right([1, 2, 3, 4], 5)
        [4, 1, 2, 3]
        >>> ba_12_rotate_right([], 10)
        []
    """
    raise ValueError("todo")


def ba_13_remove_negatives_in_place(nums: List[int]) -> None:
    """
    Category: Lists & Tuples | Tags: in-place mutation, filtering | Difficulty: 4

    Mutate nums in place to remove all negative values, preserving the order
    of the remaining elements.

    Return None.

    Examples:
        >>> xs = [3, -1, 0, -5, 2]
        >>> ba_13_remove_negatives_in_place(xs)
        >>> xs
        [3, 0, 2]
    """
    raise ValueError("todo")


def ba_14_dedup_preserve_order(nums: List[int]) -> List[int]:
    """
    Category: Lists & Tuples | Tags: dedup, preserve order | Difficulty: 3

    Return a NEW list containing the first occurrence of each distinct element
    in nums, in the order they first appeared.

    Examples:
        >>> ba_14_dedup_preserve_order([1, 2, 1, 3, 2])
        [1, 2, 3]
        >>> ba_14_dedup_preserve_order([])
        []
    """
    raise ValueError("todo")


def ba_15_pairwise_sums(xs: List[int], ys: List[int]) -> List[int]:
    """
    Category: Lists & Tuples | Tags: pairwise operations | Difficulty: 3

    Given two lists of equal length, return a NEW list where the i-th element
    is xs[i] + ys[i].

    Raise ValueError if the lists have different lengths.

    Examples:
        >>> ba_15_pairwise_sums([1, 2, 3], [10, 20, 30])
        [11, 22, 33]
    """
    raise ValueError("todo")


def ba_16_split_by_parity(nums: List[int]) -> Tuple[List[int], List[int]]:
    """
    Category: Lists & Tuples | Tags: partition, parity | Difficulty: 3

    Split nums into (evens, odds), both NEW lists, preserving relative order
    within each sub-list.

    Examples:
        >>> ba_16_split_by_parity([1, 2, 3, 4])
        ([2, 4], [1, 3])
        >>> ba_16_split_by_parity([])
        ([], [])
    """
    raise ValueError("todo")


def ba_17_chunk_list(nums: List[int], size: int) -> List[List[int]]:
    """
    Category: Lists & Tuples | Tags: chunking, nested lists | Difficulty: 4

    Break nums into chunks of length size, returning a list of these sub-lists.
    The final chunk may be shorter if len(nums) is not a multiple of size.

    Raise ValueError if size <= 0.

    Examples:
        >>> ba_17_chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    raise ValueError("todo")


def ba_18_argmax(nums: List[int]) -> Optional[int]:
    """
    Category: Lists & Tuples | Tags: search, index | Difficulty: 3

    Return the index of the maximum element in nums.
    If nums is empty, return None.
    If there are ties, return the smallest index with the maximum value.

    Examples:
        >>> ba_18_argmax([1, 5, 3, 5])
        1
        >>> ba_18_argmax([])
        None
    """
    raise ValueError("todo")


def ba_19_all_prefix_sums(nums: List[int]) -> List[int]:
    """
    Category: Lists & Tuples | Tags: prefix sums, accumulation | Difficulty: 4

    Return a NEW list p where p[i] is the sum of nums[0] + ... + nums[i].

    Examples:
        >>> ba_19_all_prefix_sums([1, 2, 3])
        [1, 3, 6]
        >>> ba_19_all_prefix_sums([])
        []
    """
    raise ValueError("todo")


def ba_20_interleave_lists(xs: List[int], ys: List[int]) -> List[int]:
    """
    Category: Lists & Tuples | Tags: interleave, indexing | Difficulty: 4

    Return a NEW list formed by interleaving elements from xs and ys:
    [xs[0], ys[0], xs[1], ys[1], ...] until one list runs out, then append
    the remaining tail of the longer list.

    Examples:
        >>> ba_20_interleave_lists([1, 2, 3], [10, 20])
        [1, 10, 2, 20, 3]
        >>> ba_20_interleave_lists([], [1, 2])
        [1, 2]
    """
    raise ValueError("todo")


# =====================================================================================
# 3) FUNCTIONS, ARGUMENTS & MUTABILITY / SCOPE
# =====================================================================================

def ba_21_increment_all_in_place(nums: List[int], delta: int) -> None:
    """
    Category: Functions & Mutability | Tags: in-place update, side effects | Difficulty: 3

    Mutate nums so that each element is increased by delta.
    Return None.

    Examples:
        >>> xs = [1, 2, 3]
        >>> ba_21_increment_all_in_place(xs, 5)
        >>> xs
        [6, 7, 8]
    """
    raise ValueError("todo")


def ba_22_increment_copy(nums: List[int], delta: int) -> List[int]:
    """
    Category: Functions & Mutability | Tags: pure function, copying | Difficulty: 3

    Return a NEW list where each element is nums[i] + delta.
    Do not mutate the input list.

    Examples:
        >>> xs = [1, 2, 3]
        >>> ys = ba_22_increment_copy(xs, 5)
        >>> xs
        [1, 2, 3]
        >>> ys
        [6, 7, 8]
    """
    raise ValueError("todo")


def ba_23_append_log(log: List[str], message: str) -> None:
    """
    Category: Functions & Mutability | Tags: in-place append | Difficulty: 2

    Append message to the log list in place. Return None.

    Examples:
        >>> log = ["start"]
        >>> ba_23_append_log(log, "step1")
        >>> log
        ['start', 'step1']
    """
    raise ValueError("todo")


def ba_24_copy_and_append(log: List[str], message: str) -> List[str]:
    """
    Category: Functions & Mutability | Tags: copying, lists | Difficulty: 3

    Return a NEW list equal to log with message appended at the end.
    Do not mutate the input list.

    Examples:
        >>> log = ["start"]
        >>> new_log = ba_24_copy_and_append(log, "step1")
        >>> log
        ['start']
        >>> new_log
        ['start', 'step1']
    """
    raise ValueError("todo")


def ba_25_update_counter(counts: Dict[str, int], key: str) -> None:
    """
    Category: Functions & Mutability | Tags: dict, in-place update | Difficulty: 3

    Given a dictionary mapping strings to integer counts, increment the count
    for key by 1 in place. If key is not present, treat its current count as 0.

    Return None.

    Examples:
        >>> d = {}
        >>> ba_25_update_counter(d, "a")
        >>> d
        {'a': 1}
        >>> ba_25_update_counter(d, "a")
        >>> d
        {'a': 2}
    """
    raise ValueError("todo")


def ba_26_clone_and_update_counter(counts: Dict[str, int], key: str) -> Dict[str, int]:
    """
    Category: Functions & Mutability | Tags: dict, copy vs. alias | Difficulty: 4

    Return a NEW dictionary based on counts, but with the count for key
    incremented by 1 (treat missing key as 0). Do not mutate counts.

    Examples:
        >>> d = {"x": 2}
        >>> new_d = ba_26_clone_and_update_counter(d, "x")
        >>> d
        {'x': 2}
        >>> new_d
        {'x': 3}
        >>> newer = ba_26_clone_and_update_counter(d, "y")
        >>> newer
        {'x': 2, 'y': 1}
    """
    raise ValueError("todo")


def ba_27_safe_pop(nums: List[int]) -> Optional[int]:
    """
    Category: Functions & Mutability | Tags: list, mutation, None | Difficulty: 3

    Remove and return the last element of nums, mutating the list.
    If nums is empty, return None and leave it unchanged.

    Examples:
        >>> xs = [1, 2, 3]
        >>> ba_27_safe_pop(xs)
        3
        >>> xs
        [1, 2, 2]  # test will check correct final state, not this doctest comment
    """
    raise ValueError("todo")


def ba_28_zero_out_below_threshold(nums: List[int], threshold: int) -> None:
    """
    Category: Functions & Mutability | Tags: in-place update, conditionals | Difficulty: 3

    Mutate nums so that any element strictly less than threshold is replaced by 0.
    Return None.

    Examples:
        >>> xs = [5, 1, 7, 3]
        >>> ba_28_zero_out_below_threshold(xs, 3)
        >>> xs
        [5, 0, 7, 3]
    """
    raise ValueError("todo")


def ba_29_extend_if_short(nums: List[int], target_len: int, fill: int = 0) -> None:
    """
    Category: Functions & Mutability | Tags: in-place, default args | Difficulty: 4

    Mutate nums in place so that its length is at least target_len.
    If len(nums) < target_len, append copies of fill until the length is target_len.
    If len(nums) >= target_len, leave it unchanged.

    Examples:
        >>> xs = [1, 2]
        >>> ba_29_extend_if_short(xs, 5, fill=9)
        >>> xs
        [1, 2, 9, 9, 9]
    """
    raise ValueError("todo")


def ba_30_normalize_scores(scores: List[float]) -> List[float]:
    """
    Category: Functions & Mutability | Tags: pure function, scaling | Difficulty: 4

    Given a non-empty list of non-negative scores, return a NEW list where each
    score is scaled so that the maximum becomes 1.0 and others are scaled
    proportionally: score / max_score.

    Do not mutate the input list.

    Raise ValueError if scores is empty.

    Examples:
        >>> ba_30_normalize_scores([0.0, 50.0, 100.0])
        [0.0, 0.5, 1.0]
    """
    raise ValueError("todo")


# =====================================================================================
# 4) CLASSES & OBJECTS (SIMPLE DATA MODELS)
# =====================================================================================

@dataclass
class Point2D:
    """
    Category: Classes & Objects | Tags: dataclass, geometry | Difficulty: 3–4

    Simple 2D point with x and y coordinates.
    """
    x: float
    y: float

    def translate(self, dx: float, dy: float) -> None:
        """
        Shift this point in place by (dx, dy).

        Examples:
            >>> p = Point2D(1.0, 2.0)
            >>> p.translate(3.0, -1.0)
            >>> (p.x, p.y)
            (4.0, 1.0)
        """
        raise ValueError("todo")

    def scaled(self, factor: float) -> "Point2D":
        """
        Return a NEW Point2D whose coordinates are this point's coordinates
        multiplied by factor. Do not mutate self.

        Examples:
            >>> p = Point2D(2.0, 3.0)
            >>> q = p.scaled(0.5)
            >>> (p.x, p.y)
            (2.0, 3.0)
            >>> (q.x, q.y)
            (1.0, 1.5)
        """
        raise ValueError("todo")

    def distance_to(self, other: "Point2D") -> float:
        """
        Return the Euclidean distance between this point and another.

        Examples:
            >>> p = Point2D(0.0, 0.0)
            >>> q = Point2D(3.0, 4.0)
            >>> p.distance_to(q)
            5.0
        """
        raise ValueError("todo")

    def __str__(self) -> str:
        """
        Return a human-readable string of the form 'Point2D(x, y)' with the
        numeric values filled in.

        Examples:
            >>> str(Point2D(1.0, 2.0))
            'Point2D(1.0, 2.0)'
        """
        raise ValueError("todo")


@dataclass
class BankAccount:
    """
    Category: Classes & Objects | Tags: state, methods | Difficulty: 3–5

    Simple bank account with an owner and balance.
    """
    owner: str
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        """
        Increase the balance by amount. Raise ValueError if amount < 0.

        Examples:
            >>> acc = BankAccount("Alice", 100.0)
            >>> acc.deposit(50.0)
            >>> acc.balance
            150.0
        """
        raise ValueError("todo")

    def withdraw(self, amount: float) -> bool:
        """
        Attempt to withdraw amount from the account.

        - If amount < 0, raise ValueError.
        - If amount <= balance, subtract it and return True.
        - If amount > balance, leave balance unchanged and return False.

        Examples:
            >>> acc = BankAccount("Bob", 40.0)
            >>> acc.withdraw(10.0)
            True
            >>> acc.balance
            30.0
            >>> acc.withdraw(100.0)
            False
            >>> acc.balance
            30.0
        """
        raise ValueError("todo")

    def transfer_to(self, other: "BankAccount", amount: float) -> bool:
        """
        Transfer amount from this account to another.

        Use withdraw on self; only if withdraw succeeds, deposit into other.
        Return True on success, False otherwise.

        Examples:
            >>> a = BankAccount("A", 50.0)
            >>> b = BankAccount("B", 0.0)
            >>> a.transfer_to(b, 20.0)
            True
            >>> (a.balance, b.balance)
            (30.0, 20.0)
        """
        raise ValueError("todo")

    def apply_interest(self, rate: float) -> None:
        """
        Apply simple interest to the account in place.

        balance <- balance * (1 + rate)

        Examples:
            >>> acc = BankAccount("C", 100.0)
            >>> acc.apply_interest(0.1)
            >>> acc.balance
            110.0
        """
        raise ValueError("todo")


@dataclass
class TodoList:
    """
    Category: Classes & Objects | Tags: collections, methods | Difficulty: 3–5

    Simple todo list tracking tasks and their completion status.

    Attributes:
        name: human-readable name for the list
        tasks: list of task descriptions (strings)
        done:  parallel list of booleans, same length as tasks
    """
    name: str
    tasks: List[str] = field(default_factory=list)
    done: List[bool] = field(default_factory=list)

    def add_task(self, description: str) -> None:
        """
        Add a new task with the given description, initially not done.

        Examples:
            >>> t = TodoList("daily")
            >>> t.add_task("write code")
            >>> t.tasks
            ['write code']
            >>> t.done
            [False]
        """
        raise ValueError("todo")

    def complete_task(self, index: int) -> None:
        """
        Mark the task at the given index as completed (True) in done.

        Raise IndexError if index is out of range.

        Examples:
            >>> t = TodoList("daily", ["a", "b"], [False, False])
            >>> t.complete_task(1)
            >>> t.done
            [False, True]
        """
        raise ValueError("todo")

    def pending_tasks(self) -> List[str]:
        """
        Return a NEW list containing descriptions of all tasks that are not done.

        Examples:
            >>> t = TodoList("daily", ["a", "b"], [True, False])
            >>> t.pending_tasks()
            ['b']
        """
        raise ValueError("todo")

    def __len__(self) -> int:
        """
        Return the number of tasks in this todo list.

        Examples:
            >>> len(TodoList("daily"))
            0
            >>> len(TodoList("daily", ["a", "b"], [False, True]))
            2
        """
        raise ValueError("todo")
