from __future__ import annotations

from typing import Any, List, Optional, Tuple


def lt_01_sum_list(nums: List[int]) -> int:
    total = 0
    for n in nums:
        total += n
    return total


def lt_02_average_list(nums: List[float]) -> Optional[float]:
    if not nums:
        return None
    total = 0.0
    for n in nums:
        total += n
    return total / len(nums)


def lt_03_max_index(nums: List[int]) -> Optional[int]:
    if not nums:
        return None
    max_idx = 0
    max_val = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
            max_idx = i
    return max_idx


def lt_04_find_all_indices(nums: List[int], target: int) -> List[int]:
    result: List[int] = []
    for i, val in enumerate(nums):
        if val == target:
            result.append(i)
    return result


def lt_05_reverse_new(seq: List[Any]) -> List[Any]:
    result: List[Any] = []
    for i in range(len(seq) - 1, -1, -1):
        result.append(seq[i])
    return result


def lt_06_reverse_in_place(seq: List[Any]) -> None:
    left, right = 0, len(seq) - 1
    while left < right:
        seq[left], seq[right] = seq[right], seq[left]
        left += 1
        right -= 1


def lt_07_is_sorted_non_decreasing(nums: List[int]) -> bool:
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


def lt_08_insert_sorted(nums: List[int], x: int) -> List[int]:
    result: List[int] = []
    inserted = False
    for val in nums:
        if not inserted and x <= val:
            result.append(x)
            inserted = True
        result.append(val)
    if not inserted:
        result.append(x)
    return result


def lt_09_remove_all(seq: List[Any], target: Any) -> List[Any]:
    return [val for val in seq if val != target]


def lt_10_dedup_preserve_order(seq: List[Any]) -> List[Any]:
    seen = set()
    result: List[Any] = []
    for val in seq:
        if val in seen:
            continue
        seen.add(val)
        result.append(val)
    return result


def lt_11_pairwise_sums(a: List[int], b: List[int]) -> List[int]:
    return [x + y for x, y in zip(a, b)]


def lt_12_dot_product(a: List[int], b: List[int]) -> int:
    total = 0
    for x, y in zip(a, b):
        total += x * y
    return total


def lt_13_prefix_sums(nums: List[int]) -> List[int]:
    result: List[int] = []
    running = 0
    for n in nums:
        running += n
        result.append(running)
    return result


def lt_14_windowed_sublists(nums: List[int], k: int) -> List[List[int]]:
    if k <= 0 or k > len(nums):
        return []
    result: List[List[int]] = []
    for i in range(len(nums) - k + 1):
        result.append(nums[i : i + k])
    return result


def lt_15_chunk_list(seq: List[Any], chunk_size: int) -> List[List[Any]]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    return [seq[i : i + chunk_size] for i in range(0, len(seq), chunk_size)]


def lt_16_zip_lists(a: List[Any], b: List[Any]) -> List[Tuple[Any, Any]]:
    limit = min(len(a), len(b))
    result: List[Tuple[Any, Any]] = []
    for i in range(limit):
        result.append((a[i], b[i]))
    return result


def lt_17_unzip_pairs(pairs: List[Tuple[Any, Any]]) -> Tuple[List[Any], List[Any]]:
    firsts: List[Any] = []
    seconds: List[Any] = []
    for x, y in pairs:
        firsts.append(x)
        seconds.append(y)
    return firsts, seconds


def lt_18_rotate_right(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if n == 0:
        return []
    k %= n
    if k == 0:
        return nums.copy()
    return nums[-k:] + nums[:-k]


def lt_19_interleave_lists(a: List[Any], b: List[Any]) -> List[Any]:
    result: List[Any] = []
    min_len = min(len(a), len(b))
    for i in range(min_len):
        result.append(a[i])
        result.append(b[i])
    if len(a) > min_len:
        result.extend(a[min_len:])
    if len(b) > min_len:
        result.extend(b[min_len:])
    return result


def lt_20_partition_by_predicate(seq: List[int]) -> Tuple[List[int], List[int]]:
    evens: List[int] = []
    odds: List[int] = []
    for val in seq:
        if val % 2 == 0:
            evens.append(val)
        else:
            odds.append(val)
    return evens, odds


def lt_21_group_by_mod(nums: List[int], m: int) -> List[List[int]]:
    if m <= 0:
        raise ValueError("m must be positive")
    buckets: List[List[int]] = [[] for _ in range(m)]
    for num in nums:
        buckets[num % m].append(num)
    return buckets


def lt_22_flatten_list_of_lists(nested: List[List[Any]]) -> List[Any]:
    flat: List[Any] = []
    for inner in nested:
        for val in inner:
            flat.append(val)
    return flat


def lt_23_transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    transposed: List[List[int]] = [[0] * rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            transposed[c][r] = matrix[r][c]
    return transposed


def lt_24_diagonal_sums(square: List[List[int]]) -> Tuple[int, int]:
    n = len(square)
    main = 0
    anti = 0
    for i in range(n):
        main += square[i][i]
        anti += square[i][n - 1 - i]
    return main, anti


def lt_25_argmin_argmax(nums: List[int]) -> Optional[Tuple[int, int]]:
    if not nums:
        return None
    min_idx = max_idx = 0
    min_val = max_val = nums[0]
    for i in range(1, len(nums)):
        val = nums[i]
        if val < min_val:
            min_val = val
            min_idx = i
        if val > max_val:
            max_val = val
            max_idx = i
    return min_idx, max_idx


def lt_26_median_of_list(nums: List[int]) -> Optional[float]:
    if not nums:
        return None
    sorted_copy = sorted(nums)
    n = len(sorted_copy)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_copy[mid])
    return (sorted_copy[mid - 1] + sorted_copy[mid]) / 2.0


def lt_27_mode_of_list(nums: List[int]) -> Optional[int]:
    if not nums:
        return None
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    best_num = None
    best_count = -1
    for num, count in counts.items():
        if count > best_count or (count == best_count and (best_num is None or num < best_num)):
            best_num = num
            best_count = count
    return best_num


def lt_28_run_length_encode_list(seq: List[Any]) -> List[Tuple[Any, int]]:
    if not seq:
        return []
    encoded: List[Tuple[Any, int]] = []
    current = seq[0]
    count = 1
    for val in seq[1:]:
        if val == current:
            count += 1
        else:
            encoded.append((current, count))
            current = val
            count = 1
    encoded.append((current, count))
    return encoded


def lt_29_expand_run_length(encoded: List[Tuple[Any, int]]) -> List[Any]:
    result: List[Any] = []
    for val, count in encoded:
        for _ in range(count):
            result.append(val)
    return result


def lt_30_unique_pairs_sum_to(nums: List[int], target: int) -> List[Tuple[int, int]]:
    pairs: List[Tuple[int, int]] = []
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] + nums[j] == target:
                a, b = nums[i], nums[j]
                if a > b:
                    a, b = b, a
                candidate = (a, b)
                if candidate not in pairs:
                    pairs.append(candidate)
    return pairs
