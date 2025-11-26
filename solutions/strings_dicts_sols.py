from __future__ import annotations

from typing import Any, Dict, List, Optional


def sd_01_count_vowels(s: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)


def sd_02_count_substring_overlap(s: str, sub: str) -> int:
    count = 0
    i = 0
    while i + len(sub) <= len(s):
        if s[i : i + len(sub)] == sub:
            count += 1
        i += 1
    return count


def sd_03_reverse_string(s: str) -> str:
    return s[::-1]


def sd_04_is_palindrome(s: str) -> bool:
    return s == s[::-1]


def sd_05_only_alpha_lower(s: str) -> str:
    return "".join(ch.lower() for ch in s if ch.isalpha())


def sd_06_split_on_spaces(s: str) -> List[str]:
    parts: List[str] = []
    current = []
    for ch in s:
        if ch == " ":
            if current:
                parts.append("".join(current))
                current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current))
    return parts


def sd_07_join_with_comma(words: List[str]) -> str:
    if not words:
        return ""
    result = words[0]
    for w in words[1:]:
        result += "," + w
    return result


def sd_08_strip_outer_spaces(s: str) -> str:
    left = 0
    right = len(s) - 1
    while left <= right and s[left] == " ":
        left += 1
    while right >= left and s[right] == " ":
        right -= 1
    return s[left : right + 1]


def sd_09_normalize_whitespace(s: str) -> str:
    tokens = sd_06_split_on_spaces(s)
    return " ".join(tokens)


def sd_10_extract_digits(s: str) -> str:
    return "".join(ch for ch in s if ch.isdigit())


def sd_11_char_frequency(s: str) -> Dict[str, int]:
    freq: Dict[str, int] = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


def sd_12_word_frequency(s: str) -> Dict[str, int]:
    words = sd_06_split_on_spaces(s)
    freq: Dict[str, int] = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def sd_13_most_frequent_char(s: str) -> Optional[str]:
    if not s:
        return None
    freq = sd_11_char_frequency(s)
    best_char = None
    best_count = -1
    for ch, count in freq.items():
        if count > best_count or (count == best_count and (best_char is None or ch < best_char)):
            best_char = ch
            best_count = count
    return best_char


def sd_14_anagram_dict(words: List[str]) -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = {}
    for w in words:
        key = "".join(sorted(w))
        groups.setdefault(key, []).append(w)
    return groups


def sd_15_group_words_by_length(words: List[str]) -> Dict[int, List[str]]:
    grouped: Dict[int, List[str]] = {}
    for w in words:
        grouped.setdefault(len(w), []).append(w)
    return grouped


def sd_16_is_anagram(a: str, b: str) -> bool:
    return sd_11_char_frequency(a) == sd_11_char_frequency(b)


def sd_17_first_unique_char(s: str) -> Optional[str]:
    freq = sd_11_char_frequency(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None


def sd_18_replace_words_dict(words: List[str], repl: Dict[str, str]) -> List[str]:
    return [repl.get(w, w) for w in words]


def sd_19_map_chars(s: str, mapping: Dict[str, str]) -> str:
    return "".join(mapping.get(ch, ch) for ch in s)


def sd_20_encode_cipher_map(s: str, mapping: Dict[str, str]) -> str:
    return sd_19_map_chars(s, mapping)


def sd_21_invert_dict(d: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    inverted: Dict[Any, List[Any]] = {}
    for k, v in d.items():
        inverted.setdefault(v, []).append(k)
    return inverted


def sd_22_merge_dicts_sum(a: Dict[str, int], b: Dict[str, int]) -> Dict[str, int]:
    merged: Dict[str, int] = {}
    for k, v in a.items():
        merged[k] = v
    for k, v in b.items():
        merged[k] = merged.get(k, 0) + v
    return merged


def sd_23_dict_filter_threshold(d: Dict[str, int], t: int) -> Dict[str, int]:
    return {k: v for k, v in d.items() if v >= t}


def sd_24_dict_argmax_value(d: Dict[str, int]) -> Optional[str]:
    if not d:
        return None
    best_key = None
    best_val = None
    for k, v in d.items():
        if best_val is None or v > best_val or (v == best_val and k < best_key):
            best_key = k
            best_val = v
    return best_key


def sd_25_histogram_even_odd(nums: List[int]) -> Dict[str, int]:
    even = sum(1 for n in nums if n % 2 == 0)
    odd = len(nums) - even
    return {"even": even, "odd": odd}


def sd_26_longest_palindromic_substring_simple(s: str) -> str:
    best = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i : j + 1]
            if substring == substring[::-1] and len(substring) > len(best):
                best = substring
    return best


def sd_27_longest_common_prefix(words: List[str]) -> str:
    if not words:
        return ""
    prefix = words[0]
    for w in words[1:]:
        while not w.startswith(prefix) and prefix:
            prefix = prefix[:-1]
        if not prefix:
            break
    return prefix


def sd_28_word_pattern(pattern: str, s: str) -> bool:
    words = sd_06_split_on_spaces(s)
    if len(pattern) != len(words):
        return False
    p_to_w: Dict[str, str] = {}
    w_to_p: Dict[str, str] = {}
    for p, w in zip(pattern, words):
        if p in p_to_w and p_to_w[p] != w:
            return False
        if w in w_to_p and w_to_p[w] != p:
            return False
        p_to_w[p] = w
        w_to_p[w] = p
    return True


def sd_29_decode_run_length_str(s: str) -> str:
    decoded: List[str] = []
    i = 0
    while i < len(s):
        ch = s[i]
        i += 1
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        if not count_str:
            raise ValueError("Missing count in run-length string")
        count = int(count_str)
        decoded.append(ch * count)
    return "".join(decoded)


def sd_30_letter_combinations_phone(digits: str) -> List[str]:
    if not digits:
        return []
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    results: List[str] = []

    def backtrack(index: int, path: List[str]) -> None:
        if index == len(digits):
            results.append("".join(path))
            return
        letters = mapping.get(digits[index], "")
        for ch in letters:
            path.append(ch)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return results
