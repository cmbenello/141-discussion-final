

"""
strings_dicts.py

Curated problem set focused on STRING manipulation and DICTIONARY-based algorithms
(CMSC 14100 exam difficulty: levels 2–5). Each function includes:
  - Category / Tags / Difficulty
  - Clear problem specification
  - Doctest-style Examples
  - Stub implementation that raises ValueError("todo")

Students implement these in problems/strings_dicts.py.
Instructor solutions live in solutions/strings_dicts_sols.py.
Tests switch using USE_SOLUTIONS=1.
"""

from __future__ import annotations
from typing import List, Dict, Tuple, Optional


# =====================================================================================
# TABLE OF CONTENTS (30 Problems)
# =====================================================================================
#
# 1) Basic String Scans & Transformations
#    - sd_01_count_vowels
#    - sd_02_count_substring_overlap
#    - sd_03_reverse_string
#    - sd_04_is_palindrome
#    - sd_05_only_alpha_lower
#
# 2) String Parsing / Tokenization
#    - sd_06_split_on_spaces
#    - sd_07_join_with_comma
#    - sd_08_strip_outer_spaces
#    - sd_09_normalize_whitespace
#    - sd_10_extract_digits
#
# 3) Dictionary Frequency & Counting
#    - sd_11_char_frequency
#    - sd_12_word_frequency
#    - sd_13_most_frequent_char
#    - sd_14_anagram_dict
#    - sd_15_group_words_by_length
#
# 4) String–Dict Combined Algorithms
#    - sd_16_is_anagram
#    - sd_17_first_unique_char
#    - sd_18_replace_words_dict
#    - sd_19_map_chars
#    - sd_20_encode_cipher_map
#
# 5) Dictionary-Based Searches & Lookups
#    - sd_21_invert_dict
#    - sd_22_merge_dicts_sum
#    - sd_23_dict_filter_threshold
#    - sd_24_dict_argmax_value
#    - sd_25_histogram_even_odd
#
# 6) Challenge Problems (Strings + Dicts)
#    - sd_26_longest_palindromic_substring_simple
#    - sd_27_longest_common_prefix
#    - sd_28_word_pattern
#    - sd_29_decode_run_length_str
#    - sd_30_letter_combinations_phone
#
# =====================================================================================


# =====================================================================================
# 1) BASIC STRING SCANS & TRANSFORMATIONS
# =====================================================================================

def sd_01_count_vowels(s: str) -> int:
    """
    Category: Basic String Scans | Tags: vowels, counting | Difficulty: 2

    Count vowels ('a','e','i','o','u' in upper/lower case) in the string s.

    Examples:
        >>> sd_01_count_vowels("abc")
        1
        >>> sd_01_count_vowels("XYZ")
        0
    """
    raise ValueError("todo")


def sd_02_count_substring_overlap(s: str, sub: str) -> int:
    """
    Category: Basic String Scans | Tags: substring, overlapping | Difficulty: 3

    Count overlapping occurrences of sub inside s.
    Precondition: len(sub) >= 1.

    Examples:
        >>> sd_02_count_substring_overlap("aaaa", "aa")
        3
        >>> sd_02_count_substring_overlap("abc", "x")
        0
    """
    raise ValueError("todo")


def sd_03_reverse_string(s: str) -> str:
    """
    Category: Basic String Scans | Tags: reverse | Difficulty: 2

    Return a new string equal to s reversed.

    Examples:
        >>> sd_03_reverse_string("abc")
        "cba"
        >>> sd_03_reverse_string("")
        ""
    """
    raise ValueError("todo")


def sd_04_is_palindrome(s: str) -> bool:
    """
    Category: Basic String Scans | Tags: palindrome | Difficulty: 2

    Return True iff s reads the same forward and backward.

    Examples:
        >>> sd_04_is_palindrome("racecar")
        True
        >>> sd_04_is_palindrome("abc")
        False
    """
    raise ValueError("todo")


def sd_05_only_alpha_lower(s: str) -> str:
    """
    Category: Basic String Scans | Tags: filter, lowercase | Difficulty: 3

    Return a new string containing only alphabetic characters of s,
    converted to lowercase, in their original order.

    Examples:
        >>> sd_05_only_alpha_lower("A1b*C")
        "abc"
        >>> sd_05_only_alpha_lower("123")
        ""
    """
    raise ValueError("todo")


# =====================================================================================
# 2) STRING PARSING / TOKENIZATION
# =====================================================================================

def sd_06_split_on_spaces(s: str) -> List[str]:
    """
    Category: Parsing | Tags: split, manual | Difficulty: 2

    Manually split s on spaces (single-space separator), ignoring empty tokens
    caused by consecutive spaces.

    Examples:
        >>> sd_06_split_on_spaces("a b  c")
        ["a", "b", "c"]
        >>> sd_06_split_on_spaces("")
        []
    """
    raise ValueError("todo")


def sd_07_join_with_comma(words: List[str]) -> str:
    """
    Category: Parsing | Tags: join | Difficulty: 2

    Manually join words with commas, no trailing comma.

    Examples:
        >>> sd_07_join_with_comma(["a","b","c"])
        "a,b,c"
        >>> sd_07_join_with_comma([])
        ""
    """
    raise ValueError("todo")


def sd_08_strip_outer_spaces(s: str) -> str:
    """
    Category: Parsing | Tags: strip | Difficulty: 2

    Remove leading and trailing spaces without using str.strip().

    Examples:
        >>> sd_08_strip_outer_spaces("  abc  ")
        "abc"
        >>> sd_08_strip_outer_spaces("abc")
        "abc"
    """
    raise ValueError("todo")


def sd_09_normalize_whitespace(s: str) -> str:
    """
    Category: Parsing | Tags: collapse_spaces | Difficulty: 3

    Normalize whitespace by replacing sequences of >=1 spaces with a single space.
    Leading/trailing spaces should be removed.

    Examples:
        >>> sd_09_normalize_whitespace("  a   b  c ")
        "a b c"
    """
    raise ValueError("todo")


def sd_10_extract_digits(s: str) -> str:
    """
    Category: Parsing | Tags: filter, digits | Difficulty: 2

    Return a string containing only digits ('0'–'9') from s.

    Examples:
        >>> sd_10_extract_digits("a1b23c")
        "123"
        >>> sd_10_extract_digits("")
        ""
    """
    raise ValueError("todo")


# =====================================================================================
# 3) DICTIONARY FREQUENCY & COUNTING
# =====================================================================================

def sd_11_char_frequency(s: str) -> Dict[str, int]:
    """
    Category: Dict Frequency | Tags: freq, characters | Difficulty: 2

    Build and return a dictionary mapping each character in s to its count.

    Examples:
        >>> sd_11_char_frequency("aba")
        {"a": 2, "b": 1}
        >>> sd_11_char_frequency("")
        {}
    """
    raise ValueError("todo")


def sd_12_word_frequency(s: str) -> Dict[str, int]:
    """
    Category: Dict Frequency | Tags: freq, words | Difficulty: 3

    Manually split s on spaces (like sd_06_split_on_spaces) and return a dict
    mapping each word to its count.

    Examples:
        >>> sd_12_word_frequency("a b a c a")
        {"a": 3, "b": 1, "c": 1}
    """
    raise ValueError("todo")


def sd_13_most_frequent_char(s: str) -> Optional[str]:
    """
    Category: Dict Frequency | Tags: max, frequency | Difficulty: 3

    Return the character that appears most frequently in s.
    Break ties by returning the alphabetically smallest character.
    If s is empty, return None.

    Examples:
        >>> sd_13_most_frequent_char("bbaac")
        "a"
        >>> sd_13_most_frequent_char("")
        None
    """
    raise ValueError("todo")


def sd_14_anagram_dict(words: List[str]) -> Dict[str, List[str]]:
    """
    Category: Dict Frequency | Tags: anagram groups | Difficulty: 4

    Group words into anagram buckets using sorted(word) as the key.

    Examples:
        >>> sd_14_anagram_dict(["eat","tea","tan","ate","nat","bat"])
        {"aet": ["eat","tea","ate"], "ant": ["tan","nat"], "abt": ["bat"]}
    """
    raise ValueError("todo")


def sd_15_group_words_by_length(words: List[str]) -> Dict[int, List[str]]:
    """
    Category: Dict Frequency | Tags: length grouping | Difficulty: 2

    Return a dict mapping each length ℓ to all words of length ℓ (preserving order).

    Examples:
        >>> sd_15_group_words_by_length(["a","to","hi","x"])
        {1: ["a","x"], 2: ["to","hi"]}
    """
    raise ValueError("todo")


# =====================================================================================
# 4) STRING–DICT COMBINED ALGORITHMS
# =====================================================================================

def sd_16_is_anagram(a: str, b: str) -> bool:
    """
    Category: Combined Algorithms | Tags: sort, frequency | Difficulty: 3

    Return True iff a and b are anagrams (same letters in any order/same counts).

    Examples:
        >>> sd_16_is_anagram("listen","silent")
        True
        >>> sd_16_is_anagram("abc","abz")
        False
    """
    raise ValueError("todo")


def sd_17_first_unique_char(s: str) -> Optional[str]:
    """
    Category: Combined Algorithms | Tags: uniqueness | Difficulty: 3

    Return the first character in s whose count in s is exactly 1.
    If none exists, return None.

    Examples:
        >>> sd_17_first_unique_char("aabbcd")
        "c"
        >>> sd_17_first_unique_char("aabb")
        None
    """
    raise ValueError("todo")


def sd_18_replace_words_dict(words: List[str], repl: Dict[str, str]) -> List[str]:
    """
    Category: Combined Algorithms | Tags: replace, lookup | Difficulty: 3

    Return a NEW list where each word is replaced by repl[word] if present,
    otherwise unchanged.

    Examples:
        >>> sd_18_replace_words_dict(["a","b","c"], {"b":"beta"})
        ["a","beta","c"]
    """
    raise ValueError("todo")


def sd_19_map_chars(s: str, mapping: Dict[str, str]) -> str:
    """
    Category: Combined Algorithms | Tags: char map | Difficulty: 3

    Map each character ch in s to mapping[ch] if present, else keep original.

    Examples:
        >>> sd_19_map_chars("abc", {"a":"1","c":"9"})
        "1b9"
    """
    raise ValueError("todo")


def sd_20_encode_cipher_map(s: str, mapping: Dict[str, str]) -> str:
    """
    Category: Combined Algorithms | Tags: cipher, mapping | Difficulty: 4

    Encode s by replacing characters according to mapping. Characters not in the
    dictionary remain unchanged. Mapping values must be single-character strings.

    Examples:
        >>> sd_20_encode_cipher_map("abca", {"a":"x","c":"y"})
        "xb yx"[0:4]  # doctest visual; actual output "xbyx"
    """
    raise ValueError("todo")


# =====================================================================================
# 5) DICTIONARY-BASED SEARCHES / LOOKUPS
# =====================================================================================

def sd_21_invert_dict(d: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    """
    Category: Dict Search | Tags: invert, grouping | Difficulty: 3

    Invert dictionary d: map each value v to a list of all keys k such that d[k] == v.

    Examples:
        >>> sd_21_invert_dict({"a":1,"b":2,"c":1})
        {1:["a","c"], 2:["b"]}
    """
    raise ValueError("todo")


def sd_22_merge_dicts_sum(a: Dict[str, int], b: Dict[str, int]) -> Dict[str, int]:
    """
    Category: Dict Search | Tags: merge, sum values | Difficulty: 3

    Merge two dicts a and b, summing values for keys that appear in both.

    Examples:
        >>> sd_22_merge_dicts_sum({"x":1,"y":2}, {"y":5,"z":3})
        {"x":1,"y":7,"z":3}
    """
    raise ValueError("todo")


def sd_23_dict_filter_threshold(d: Dict[str, int], t: int) -> Dict[str, int]:
    """
    Category: Dict Search | Tags: filter | Difficulty: 2

    Return a new dict containing only entries where value >= t.

    Examples:
        >>> sd_23_dict_filter_threshold({"a":2,"b":5,"c":1}, 2)
        {"a":2,"b":5}
    """
    raise ValueError("todo")


def sd_24_dict_argmax_value(d: Dict[str, int]) -> Optional[str]:
    """
    Category: Dict Search | Tags: argmax | Difficulty: 3

    Return key with largest value in d; break ties by taking alphabetically
    smallest key. If d is empty, return None.

    Examples:
        >>> sd_24_dict_argmax_value({"a":3,"b":3,"c":2})
        "a"
        >>> sd_24_dict_argmax_value({})
        None
    """
    raise ValueError("todo")


def sd_25_histogram_even_odd(nums: List[int]) -> Dict[str, int]:
    """
    Category: Dict Search | Tags: histogram | Difficulty: 2

    Return a dict {"even": count_even, "odd": count_odd} for nums.

    Examples:
        >>> sd_25_histogram_even_odd([1,2,3,4])
        {"even":2,"odd":2}
    """
    raise ValueError("todo")


# =====================================================================================
# 6) CHALLENGE PROBLEMS (Strings + Dicts)
# =====================================================================================

def sd_26_longest_palindromic_substring_simple(s: str) -> str:
    """
    Category: Challenge | Tags: palindrome, substring | Difficulty: 5

    Return the longest palindromic substring of s using a simple O(n^3)
    approach: try all substrings and check if palindrome.

    Examples:
        >>> sd_26_longest_palindromic_substring_simple("babad") in ["bab","aba"]
        True
        >>> sd_26_longest_palindromic_substring_simple("cbbd")
        "bb"
    """
    raise ValueError("todo")


def sd_27_longest_common_prefix(words: List[str]) -> str:
    """
    Category: Challenge | Tags: prefix | Difficulty: 4

    Return the longest common prefix of all words. If words is empty, return "".

    Examples:
        >>> sd_27_longest_common_prefix(["flower","flow","flight"])
        "fl"
        >>> sd_27_longest_common_prefix([])
        ""
    """
    raise ValueError("todo")


def sd_28_word_pattern(pattern: str, s: str) -> bool:
    """
    Category: Challenge | Tags: bijection, pattern | Difficulty: 5

    Given pattern like "abba" and string s like "dog cat cat dog", return True
    iff there exists a bijection between characters in pattern and words in s.

    Examples:
        >>> sd_28_word_pattern("abba", "dog cat cat dog")
        True
        >>> sd_28_word_pattern("abba", "dog cat cat fish")
        False
    """
    raise ValueError("todo")


def sd_29_decode_run_length_str(s: str) -> str:
    """
    Category: Challenge | Tags: run-length, decode | Difficulty: 4

    Decode s where digits represent counts and letters represent symbols.
    For example: "a3b1c2" ⇒ "aaabcc".

    Examples:
        >>> sd_29_decode_run_length_str("a3b1c2")
        "aaabcc"
        >>> sd_29_decode_run_length_str("")
        ""
    """
    raise ValueError("todo")


def sd_30_letter_combinations_phone(digits: str) -> List[str]:
    """
    Category: Challenge | Tags: backtracking, phone keypad | Difficulty: 5

    Given a digit string where each digit maps to certain letters (like classic
    phone keypad), return all possible letter combinations.

    Use mapping:
        2: "abc", 3: "def", 4: "ghi", 5: "jkl",
        6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz".

    Empty input → return [].

    Examples:
        >>> sorted(sd_30_letter_combinations_phone("23"))
        ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    """
    raise ValueError("todo")