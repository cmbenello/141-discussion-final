from __future__ import annotations

import importlib
import os

import pytest
import math


USE_SOLUTIONS = os.getenv("USE_SOLUTIONS") == "1"
MODULE = importlib.import_module("solutions.basics_sols" if USE_SOLUTIONS else "problems.basics")

ba_01_add_three = MODULE.ba_01_add_three
ba_02_safe_int_div = MODULE.ba_02_safe_int_div
ba_03_average_ignore_none = MODULE.ba_03_average_ignore_none
ba_04_clamp = MODULE.ba_04_clamp
ba_05_quadratic_eval = MODULE.ba_05_quadratic_eval
ba_06_is_close = MODULE.ba_06_is_close
ba_07_to_bool_list = MODULE.ba_07_to_bool_list
ba_08_parse_rgb_hex = MODULE.ba_08_parse_rgb_hex
ba_09_seconds_to_hms = MODULE.ba_09_seconds_to_hms
ba_10_hms_to_seconds = MODULE.ba_10_hms_to_seconds
ba_11_first_last = MODULE.ba_11_first_last
ba_12_rotate_right = MODULE.ba_12_rotate_right
ba_13_remove_negatives_in_place = MODULE.ba_13_remove_negatives_in_place
ba_14_dedup_preserve_order = MODULE.ba_14_dedup_preserve_order
ba_15_pairwise_sums = MODULE.ba_15_pairwise_sums
ba_16_split_by_parity = MODULE.ba_16_split_by_parity
ba_17_chunk_list = MODULE.ba_17_chunk_list
ba_18_argmax = MODULE.ba_18_argmax
ba_19_all_prefix_sums = MODULE.ba_19_all_prefix_sums
ba_20_interleave_lists = MODULE.ba_20_interleave_lists
ba_21_increment_all_in_place = MODULE.ba_21_increment_all_in_place
ba_22_increment_copy = MODULE.ba_22_increment_copy
ba_23_append_log = MODULE.ba_23_append_log
ba_24_copy_and_append = MODULE.ba_24_copy_and_append
ba_25_update_counter = MODULE.ba_25_update_counter
ba_26_clone_and_update_counter = MODULE.ba_26_clone_and_update_counter
ba_27_safe_pop = MODULE.ba_27_safe_pop
ba_28_zero_out_below_threshold = MODULE.ba_28_zero_out_below_threshold
ba_29_extend_if_short = MODULE.ba_29_extend_if_short
ba_30_normalize_scores = MODULE.ba_30_normalize_scores
Point2D = MODULE.Point2D
BankAccount = MODULE.BankAccount
TodoList = MODULE.TodoList


def test_basic_expressions_and_types():
    assert ba_01_add_three(1, 2, 3) == 6
    assert ba_02_safe_int_div(7, 2) == 3
    assert ba_02_safe_int_div(5, 0) is None
    assert ba_03_average_ignore_none([1.0, None, 3.0]) == 2.0
    assert ba_03_average_ignore_none([None, None]) is None
    assert ba_04_clamp(5, 0, 10) == 5
    assert ba_04_clamp(-3, 0, 10) == 0
    assert ba_05_quadratic_eval(1.0, 0.0, 0.0, 2.0) == 4.0
    assert ba_06_is_close(1.0, 1.0000001) is True
    assert ba_06_is_close(1.0, 1.1) is False
    assert ba_07_to_bool_list("1010") == [1, 0, 1, 0]
    with pytest.raises(ValueError):
        ba_07_to_bool_list("10a")
    assert ba_08_parse_rgb_hex("#000000") == (0, 0, 0)
    assert ba_08_parse_rgb_hex("#FF00ff") == (255, 0, 255)
    with pytest.raises(ValueError):
        ba_08_parse_rgb_hex("123456")
    assert ba_09_seconds_to_hms(3661) == (1, 1, 1)
    assert ba_10_hms_to_seconds(1, 1, 1) == 3661


def test_lists_and_tuples():
    assert ba_11_first_last([]) is None
    assert ba_11_first_last([1, 2, 3]) == (1, 3)
    assert ba_12_rotate_right([1, 2, 3, 4], 1) == [4, 1, 2, 3]
    assert ba_13_remove_negatives_in_place([1, -2, 3]) is None
    data = [1, -2, 3]
    ba_13_remove_negatives_in_place(data)
    assert data == [1, 3]
    assert ba_14_dedup_preserve_order([1, 2, 1, 3, 2]) == [1, 2, 3]
    assert ba_15_pairwise_sums([1, 2], [3, 4]) == [4, 6]
    assert ba_16_split_by_parity([1, 2, 3, 4]) == ([2, 4], [1, 3])
    assert ba_17_chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    with pytest.raises(ValueError):
        ba_17_chunk_list([1, 2], 0)
    assert ba_18_argmax([1, 3, 2]) == 1
    assert ba_18_argmax([]) is None
    assert ba_19_all_prefix_sums([1, 2, 3]) == [1, 3, 6]
    assert ba_20_interleave_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_functions_and_mutability():
    nums = [1, 2]
    ba_21_increment_all_in_place(nums, 3)
    assert nums == [4, 5]
    assert ba_22_increment_copy([1, 2], 3) == [4, 5]
    log = []
    ba_23_append_log(log, "entry")
    assert log == ["entry"]
    new_log = ba_24_copy_and_append(log, "next")
    assert log == ["entry"] and new_log == ["entry", "next"]
    counter: Dict[str, int] = {}
    ba_25_update_counter(counter, "a", 2)
    assert counter == {"a": 2}
    new_counter = ba_26_clone_and_update_counter(counter, "a", 3)
    assert counter == {"a": 2} and new_counter == {"a": 5}
    assert ba_27_safe_pop([]) is None
    nums2 = [1, 2, 3]
    assert ba_27_safe_pop(nums2) == 3 and nums2 == [1, 2]
    nums3 = [1, 2, 3]
    ba_28_zero_out_below_threshold(nums3, 3)
    assert nums3 == [0, 0, 3]
    nums4: List[int] = []
    ba_29_extend_if_short(nums4, 3, 9)
    assert nums4 == [9, 9, 9]
    assert ba_30_normalize_scores([]) == []
    assert ba_30_normalize_scores([1, 1]) == [0.5, 0.5]


def test_point2d():
    p = Point2D(1.0, 2.0)
    p.translate(1.0, -1.0)
    assert ba_06_is_close(p.x, 2.0) and ba_06_is_close(p.y, 1.0)
    q = p.scaled(2.0)
    assert q.x == 4.0 and q.y == 2.0
    assert ba_06_is_close(p.distance_to(q), math.hypot(2.0, 1.0))
    assert str(p) == "(2.0, 1.0)"


def test_bank_account_and_todo():
    acct = BankAccount("Alice", 100.0, 0.1)
    acct.deposit(50)
    assert acct.balance == 150.0
    assert acct.withdraw(200) is False
    assert acct.withdraw(50) is True
    assert acct.balance == 100.0
    other = BankAccount("Bob", 0.0, 0.0)
    assert acct.transfer_to(other, 30) is True
    assert acct.balance == 70.0 and other.balance == 30.0
    acct.apply_interest()
    assert ba_06_is_close(acct.balance, 77.0)
    with pytest.raises(ValueError):
        acct.deposit(-1)
    with pytest.raises(ValueError):
        acct.withdraw(-1)
    with pytest.raises(ValueError):
        BankAccount("X", 0, -0.1).apply_interest()

    todos = TodoList()
    todos.add_task("task1")
    todos.add_task("task2")
    assert len(todos) == 2
    assert todos.complete_task("task1") is True
    assert todos.complete_task("missing") is False
    assert todos.pending_tasks() == ["task2"]
