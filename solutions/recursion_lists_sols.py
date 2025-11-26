from __future__ import annotations

from typing import Any, List, Optional, Tuple


def rl_01_len_recursive(xs: List[Any]) -> int:
    if not xs:
        return 0
    return 1 + rl_01_len_recursive(xs[1:])


def rl_02_sum_recursive(xs: List[int]) -> int:
    if not xs:
        return 0
    return xs[0] + rl_02_sum_recursive(xs[1:])


def rl_03_count_occurrences(xs: List[Any], target: Any) -> int:
    if not xs:
        return 0
    return (1 if xs[0] == target else 0) + rl_03_count_occurrences(xs[1:], target)


def rl_04_contains(xs: List[Any], target: Any) -> bool:
    if not xs:
        return False
    if xs[0] == target:
        return True
    return rl_04_contains(xs[1:], target)


def rl_05_all_positive(xs: List[int]) -> bool:
    if not xs:
        return True
    if xs[0] <= 0:
        return False
    return rl_05_all_positive(xs[1:])


def rl_06_any_negative(xs: List[int]) -> bool:
    if not xs:
        return False
    if xs[0] < 0:
        return True
    return rl_06_any_negative(xs[1:])


def rl_07_max_recursive(xs: List[int]) -> Optional[int]:
    if not xs:
        return None
    if len(xs) == 1:
        return xs[0]
    rest_max = rl_07_max_recursive(xs[1:])
    if rest_max is None or xs[0] > rest_max:
        return xs[0]
    return rest_max


def rl_08_min_recursive(xs: List[int]) -> Optional[int]:
    if not xs:
        return None
    if len(xs) == 1:
        return xs[0]
    rest_min = rl_08_min_recursive(xs[1:])
    if rest_min is None or xs[0] < rest_min:
        return xs[0]
    return rest_min


def rl_09_index_of_first(xs: List[Any], target: Any) -> Optional[int]:
    if not xs:
        return None
    if xs[0] == target:
        return 0
    tail_index = rl_09_index_of_first(xs[1:], target)
    if tail_index is None:
        return None
    return 1 + tail_index


def rl_10_index_of_last(xs: List[Any], target: Any) -> Optional[int]:
    if not xs:
        return None
    tail_index = rl_10_index_of_last(xs[1:], target)
    if tail_index is not None:
        return 1 + tail_index
    if xs[0] == target:
        return 0
    return None


def rl_11_copy_list(xs: List[Any]) -> List[Any]:
    if not xs:
        return []
    return [xs[0]] + rl_11_copy_list(xs[1:])


def rl_12_reverse_new(xs: List[Any]) -> List[Any]:
    if not xs:
        return []
    return rl_12_reverse_new(xs[1:]) + [xs[0]]


def rl_13_increment_all(xs: List[int], k: int) -> List[int]:
    if not xs:
        return []
    return [xs[0] + k] + rl_13_increment_all(xs[1:], k)


def rl_14_filter_even(xs: List[int]) -> List[int]:
    if not xs:
        return []
    rest = rl_14_filter_even(xs[1:])
    if xs[0] % 2 == 0:
        return [xs[0]] + rest
    return rest


def rl_15_remove_target(xs: List[Any], target: Any) -> List[Any]:
    if not xs:
        return []
    rest = rl_15_remove_target(xs[1:], target)
    if xs[0] == target:
        return rest
    return [xs[0]] + rest


def rl_16_take_first_n(xs: List[Any], n: int) -> List[Any]:
    if n <= 0 or not xs:
        return []
    return [xs[0]] + rl_16_take_first_n(xs[1:], n - 1)


def rl_17_drop_first_n(xs: List[Any], n: int) -> List[Any]:
    if not xs:
        return []
    if n <= 0:
        return rl_11_copy_list(xs)
    return rl_17_drop_first_n(xs[1:], n - 1)


def rl_18_concat_lists(a: List[Any], b: List[Any]) -> List[Any]:
    if not a:
        return rl_11_copy_list(b)
    return [a[0]] + rl_18_concat_lists(a[1:], b)


def rl_19_interleave_recursive(a: List[Any], b: List[Any]) -> List[Any]:
    if not a and not b:
        return []
    if not a:
        return rl_11_copy_list(b)
    if not b:
        return rl_11_copy_list(a)
    return [a[0], b[0]] + rl_19_interleave_recursive(a[1:], b[1:])


def rl_20_flatten_shallow(nested: List[List[Any]]) -> List[Any]:
    if not nested:
        return []
    return rl_11_copy_list(nested[0]) + rl_20_flatten_shallow(nested[1:])


def rl_21_binary_search_recursive(sorted_xs: List[int], target: int) -> bool:
    if not sorted_xs:
        return False
    mid = len(sorted_xs) // 2
    mid_val = sorted_xs[mid]
    if mid_val == target:
        return True
    if target < mid_val:
        return rl_21_binary_search_recursive(sorted_xs[:mid], target)
    return rl_21_binary_search_recursive(sorted_xs[mid + 1 :], target)


def rl_22_merge_two_sorted_recursive(a: List[int], b: List[int]) -> List[int]:
    if not a:
        return rl_11_copy_list(b)
    if not b:
        return rl_11_copy_list(a)
    if a[0] <= b[0]:
        return [a[0]] + rl_22_merge_two_sorted_recursive(a[1:], b)
    return [b[0]] + rl_22_merge_two_sorted_recursive(a, b[1:])


def rl_23_merge_sort_recursive(xs: List[int]) -> List[int]:
    if len(xs) <= 1:
        return rl_11_copy_list(xs)
    mid = len(xs) // 2
    left_sorted = rl_23_merge_sort_recursive(xs[:mid])
    right_sorted = rl_23_merge_sort_recursive(xs[mid:])
    return rl_22_merge_two_sorted_recursive(left_sorted, right_sorted)


def rl_24_is_sorted_recursive(xs: List[int]) -> bool:
    if len(xs) <= 1:
        return True
    if xs[0] > xs[1]:
        return False
    return rl_24_is_sorted_recursive(xs[1:])


def rl_25_count_inversions_simple(xs: List[int]) -> int:
    if len(xs) <= 1:
        return 0
    head = xs[0]
    tail = xs[1:]
    inversions_with_head = sum(1 for val in tail if val < head)
    return inversions_with_head + rl_25_count_inversions_simple(tail)


def rl_26_count_smaller_to_right(xs: List[int]) -> List[int]:
    if not xs:
        return []
    head = xs[0]
    tail = xs[1:]
    count_smaller = sum(1 for val in tail if val < head)
    return [count_smaller] + rl_26_count_smaller_to_right(tail)


def rl_27_max_subarray_sum_simple(xs: List[int]) -> Optional[int]:
    if not xs:
        return None

    def helper(seq: List[int]) -> Tuple[int, int]:
        if len(seq) == 1:
            return seq[0], seq[0]
        tail_max_end, tail_best = helper(seq[1:])
        max_ending_here = max(seq[0], seq[0] + tail_max_end)
        best = max(max_ending_here, tail_best)
        return max_ending_here, best

    _, best_overall = helper(xs)
    return best_overall


def rl_28_split_even_odd_indices(xs: List[Any]) -> Tuple[List[Any], List[Any]]:
    if not xs:
        return [], []
    evens_tail, odds_tail = rl_28_split_even_odd_indices(xs[1:])
    return [xs[0]] + odds_tail, evens_tail


def rl_29_find_min_max_recursive(xs: List[int]) -> Optional[Tuple[int, int]]:
    if not xs:
        return None
    if len(xs) == 1:
        return xs[0], xs[0]
    tail_min_max = rl_29_find_min_max_recursive(xs[1:])
    if tail_min_max is None:
        return xs[0], xs[0]
    tail_min, tail_max = tail_min_max
    return (xs[0] if xs[0] < tail_min else tail_min, xs[0] if xs[0] > tail_max else tail_max)


def rl_30_rotate_left_recursive(xs: List[Any], k: int) -> List[Any]:
    n = len(xs)
    if n == 0:
        return []
    k %= n
    if k == 0:
        return rl_11_copy_list(xs)
    return rl_30_rotate_left_recursive(xs[1:] + [xs[0]], k - 1)


def rl_31_len_from_index(xs: List[Any], i: int) -> int:
    if i >= len(xs):
        return 0
    return 1 + rl_31_len_from_index(xs, i + 1)


def rl_32_sum_from_index(xs: List[int], i: int) -> int:
    if i >= len(xs):
        return 0
    return xs[i] + rl_32_sum_from_index(xs, i + 1)


def rl_33_is_palindrome_list(xs: List[Any]) -> bool:
    def helper(left: int, right: int) -> bool:
        if left >= right:
            return True
        if xs[left] != xs[right]:
            return False
        return helper(left + 1, right - 1)

    return helper(0, len(xs) - 1)


def rl_34_lists_equal(a: List[Any], b: List[Any]) -> bool:
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a[0] != b[0]:
        return False
    return rl_34_lists_equal(a[1:], b[1:])


def rl_35_zip_lists_recursive(a: List[Any], b: List[Any]) -> List[Tuple[Any, Any]]:
    if not a or not b:
        return []
    return [(a[0], b[0])] + rl_35_zip_lists_recursive(a[1:], b[1:])


def rl_36_unzip_pairs_recursive(pairs: List[Tuple[Any, Any]]) -> Tuple[List[Any], List[Any]]:
    if not pairs:
        return [], []
    firsts_tail, seconds_tail = rl_36_unzip_pairs_recursive(pairs[1:])
    first, second = pairs[0]
    return [first] + firsts_tail, [second] + seconds_tail


def rl_37_all_prefixes(xs: List[Any]) -> List[List[Any]]:
    if not xs:
        return [[]]
    prefixes_without_last = rl_37_all_prefixes(xs[:-1])
    return prefixes_without_last + [prefixes_without_last[-1] + [xs[-1]]]


def rl_38_all_suffixes(xs: List[Any]) -> List[List[Any]]:
    if not xs:
        return [[]]
    return [rl_11_copy_list(xs)] + rl_38_all_suffixes(xs[1:])


def rl_39_split_at_index(xs: List[Any], k: int) -> Tuple[List[Any], List[Any]]:
    if k <= 0 or not xs:
        return [], rl_11_copy_list(xs)
    prefix, suffix = rl_39_split_at_index(xs[1:], k - 1)
    return [xs[0]] + prefix, suffix


def rl_40_run_length_encode_recursive(xs: List[Any]) -> List[Tuple[Any, int]]:
    if not xs:
        return []

    def helper(rest: List[Any], current: Any, count: int) -> List[Tuple[Any, int]]:
        if not rest:
            return [(current, count)]
        head = rest[0]
        if head == current:
            return helper(rest[1:], current, count + 1)
        return [(current, count)] + helper(rest[1:], head, 1)

    return helper(xs[1:], xs[0], 1)


def rl_41_total_length_nested(nested: List[Any]) -> int:
    total = 0
    for item in nested:
        if isinstance(item, list):
            total += rl_41_total_length_nested(item)
        else:
            total += 1
    return total


def rl_42_sum_nested_ints(nested: List[Any]) -> int:
    total = 0
    for item in nested:
        if isinstance(item, list):
            total += rl_42_sum_nested_ints(item)
        elif isinstance(item, int):
            total += item
    return total


def rl_43_flatten_nested(nested: List[Any]) -> List[Any]:
    flat: List[Any] = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(rl_43_flatten_nested(item))
        else:
            flat.append(item)
    return flat


def rl_44_max_depth_nested(nested: List[Any]) -> int:
    if not isinstance(nested, list):
        return 0
    if not nested:
        return 1
    return 1 + max(rl_44_max_depth_nested(item) for item in nested)


def rl_45_contains_in_nested(nested: List[Any], target: Any) -> bool:
    for item in nested:
        if isinstance(item, list):
            if rl_45_contains_in_nested(item, target):
                return True
        elif item == target:
            return True
    return False


def rl_46_subsets_all(xs: List[Any]) -> List[List[Any]]:
    if not xs:
        return [[]]
    rest_subsets = rl_46_subsets_all(xs[1:])
    with_first = [[xs[0]] + sub for sub in rest_subsets]
    return rest_subsets + with_first


def rl_47_permutations_all(xs: List[Any]) -> List[List[Any]]:
    if not xs:
        return [[]]
    perms: List[List[Any]] = []
    for i, val in enumerate(xs):
        remaining = xs[:i] + xs[i + 1 :]
        for perm in rl_47_permutations_all(remaining):
            perms.append([val] + perm)
    return perms


def rl_48_can_reach_sum_by_signs(xs: List[int], target: int) -> bool:
    if not xs:
        return target == 0
    first = xs[0]
    rest = xs[1:]
    return rl_48_can_reach_sum_by_signs(rest, target - first) or rl_48_can_reach_sum_by_signs(
        rest, target + first
    )


def rl_49_split_into_two_equal_sum(xs: List[int]) -> bool:
    def helper(index: int, diff: int) -> bool:
        if index == len(xs):
            return diff == 0
        val = xs[index]
        return helper(index + 1, diff + val) or helper(index + 1, diff - val)

    return helper(0, 0)


def rl_50_all_ways_to_split_into_runs(xs: List[Any]) -> List[List[List[Any]]]:
    if not xs:
        return [[]]
    all_splits: List[List[List[Any]]] = []
    for i in range(1, len(xs) + 1):
        first_segment = xs[:i]
        for rest in rl_50_all_ways_to_split_into_runs(xs[i:]):
            all_splits.append([first_segment] + rest)
    return all_splits
