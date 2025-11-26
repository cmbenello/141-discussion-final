from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


def ba_01_add_three(a: int, b: int, c: int) -> int:
    return a + b + c


def ba_02_safe_int_div(n: int, d: int) -> Optional[int]:
    if d == 0:
        return None
    return n // d


def ba_03_average_ignore_none(values: List[Optional[float]]) -> Optional[float]:
    total = 0.0
    count = 0
    for v in values:
        if v is not None:
            total += v
            count += 1
    if count == 0:
        return None
    return total / count


def ba_04_clamp(x: int, lo: int, hi: int) -> int:
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x


def ba_05_quadratic_eval(a: float, b: float, c: float, x: float) -> float:
    return a * x * x + b * x + c


def ba_06_is_close(a: float, b: float, eps: float = 1e-6) -> bool:
    return abs(a - b) <= eps


def ba_07_to_bool_list(bits: str) -> List[int]:
    result: List[int] = []
    for ch in bits:
        if ch not in {"0", "1"}:
            raise ValueError("Invalid bit character")
        result.append(int(ch))
    return result


def ba_08_parse_rgb_hex(code: str) -> Tuple[int, int, int]:
    if len(code) != 7 or not code.startswith("#"):
        raise ValueError("Invalid format")
    hex_part = code[1:]
    try:
        r = int(hex_part[0:2], 16)
        g = int(hex_part[2:4], 16)
        b = int(hex_part[4:6], 16)
    except ValueError:
        raise ValueError("Invalid hex digits") from None
    return r, g, b


def ba_09_seconds_to_hms(total: int) -> Tuple[int, int, int]:
    hours = total // 3600
    remainder = total % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return hours, minutes, seconds


def ba_10_hms_to_seconds(h: int, m: int, s: int) -> int:
    return h * 3600 + m * 60 + s


def ba_11_first_last(items: List[int]) -> Optional[Tuple[int, int]]:
    if not items:
        return None
    return items[0], items[-1]


def ba_12_rotate_right(items: List[int], k: int) -> List[int]:
    if not items:
        return []
    k %= len(items)
    return items[-k:] + items[:-k]


def ba_13_remove_negatives_in_place(nums: List[int]) -> None:
    i = 0
    while i < len(nums):
        if nums[i] < 0:
            nums.pop(i)
        else:
            i += 1


def ba_14_dedup_preserve_order(items: List[int]) -> List[int]:
    seen = set()
    result: List[int] = []
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


def ba_15_pairwise_sums(a: List[int], b: List[int]) -> List[int]:
    return [x + y for x, y in zip(a, b)]


def ba_16_split_by_parity(nums: List[int]) -> Tuple[List[int], List[int]]:
    evens: List[int] = []
    odds: List[int] = []
    for n in nums:
        (evens if n % 2 == 0 else odds).append(n)
    return evens, odds


def ba_17_chunk_list(items: List[int], size: int) -> List[List[int]]:
    if size <= 0:
        raise ValueError("size must be positive")
    return [items[i : i + size] for i in range(0, len(items), size)]


def ba_18_argmax(nums: List[int]) -> Optional[int]:
    if not nums:
        return None
    best_idx = 0
    best_val = nums[0]
    for i, val in enumerate(nums[1:], start=1):
        if val > best_val:
            best_val = val
            best_idx = i
    return best_idx


def ba_19_all_prefix_sums(nums: List[int]) -> List[int]:
    result: List[int] = []
    running = 0
    for n in nums:
        running += n
        result.append(running)
    return result


def ba_20_interleave_lists(a: List[int], b: List[int]) -> List[int]:
    result: List[int] = []
    min_len = min(len(a), len(b))
    for i in range(min_len):
        result.append(a[i])
        result.append(b[i])
    result.extend(a[min_len:])
    result.extend(b[min_len:])
    return result


def ba_21_increment_all_in_place(nums: List[int], k: int) -> None:
    for i in range(len(nums)):
        nums[i] += k


def ba_22_increment_copy(nums: List[int], k: int) -> List[int]:
    return [n + k for n in nums]


def ba_23_append_log(log: List[str], entry: str) -> None:
    log.append(entry)


def ba_24_copy_and_append(log: List[str], entry: str) -> List[str]:
    return log + [entry]


def ba_25_update_counter(counter: Dict[str, int], key: str, delta: int) -> None:
    counter[key] = counter.get(key, 0) + delta


def ba_26_clone_and_update_counter(counter: Dict[str, int], key: str, delta: int) -> Dict[str, int]:
    new_counter = dict(counter)
    new_counter[key] = new_counter.get(key, 0) + delta
    return new_counter


def ba_27_safe_pop(nums: List[int]) -> Optional[int]:
    if not nums:
        return None
    return nums.pop()


def ba_28_zero_out_below_threshold(nums: List[int], threshold: int) -> None:
    for i, val in enumerate(nums):
        if val < threshold:
            nums[i] = 0


def ba_29_extend_if_short(nums: List[int], desired_len: int, fill_value: int) -> None:
    while len(nums) < desired_len:
        nums.append(fill_value)


def ba_30_normalize_scores(scores: List[float]) -> List[float]:
    if not scores:
        return []
    total = sum(scores)
    if total == 0:
        return [0.0 for _ in scores]
    return [s / total for s in scores]


@dataclass
class Point2D:
    x: float
    y: float

    def translate(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def scaled(self, factor: float) -> "Point2D":
        return Point2D(self.x * factor, self.y * factor)

    def distance_to(self, other: "Point2D") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0
    interest_rate: float = 0.0

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def transfer_to(self, other: "BankAccount", amount: float) -> bool:
        if self.withdraw(amount):
            other.deposit(amount)
            return True
        return False

    def apply_interest(self) -> None:
        if self.interest_rate < 0:
            raise ValueError("interest_rate must be non-negative")
        self.balance += self.balance * self.interest_rate


@dataclass
class TodoList:
    tasks: List[str] = field(default_factory=list)
    completed: List[str] = field(default_factory=list)

    def add_task(self, task: str) -> None:
        self.tasks.append(task)

    def complete_task(self, task: str) -> bool:
        if task in self.tasks:
            self.tasks.remove(task)
            self.completed.append(task)
            return True
        return False

    def pending_tasks(self) -> List[str]:
        return list(self.tasks)

    def __len__(self) -> int:
        return len(self.tasks)
