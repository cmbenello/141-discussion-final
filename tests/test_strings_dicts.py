from __future__ import annotations

import importlib
import os

import pytest


USE_SOLUTIONS = os.getenv("USE_SOLUTIONS") == "1"
MODULE = importlib.import_module(
    "solutions.strings_dicts_sols" if USE_SOLUTIONS else "problems.strings_dicts"
)

sd_01_count_vowels = MODULE.sd_01_count_vowels
sd_02_count_substring_overlap = MODULE.sd_02_count_substring_overlap
sd_03_reverse_string = MODULE.sd_03_reverse_string
sd_04_is_palindrome = MODULE.sd_04_is_palindrome
sd_05_only_alpha_lower = MODULE.sd_05_only_alpha_lower
sd_06_split_on_spaces = MODULE.sd_06_split_on_spaces
sd_07_join_with_comma = MODULE.sd_07_join_with_comma
sd_08_strip_outer_spaces = MODULE.sd_08_strip_outer_spaces
sd_09_normalize_whitespace = MODULE.sd_09_normalize_whitespace
sd_10_extract_digits = MODULE.sd_10_extract_digits
sd_11_char_frequency = MODULE.sd_11_char_frequency
sd_12_word_frequency = MODULE.sd_12_word_frequency
sd_13_most_frequent_char = MODULE.sd_13_most_frequent_char
sd_14_anagram_dict = MODULE.sd_14_anagram_dict
sd_15_group_words_by_length = MODULE.sd_15_group_words_by_length
sd_16_is_anagram = MODULE.sd_16_is_anagram
sd_17_first_unique_char = MODULE.sd_17_first_unique_char
sd_18_replace_words_dict = MODULE.sd_18_replace_words_dict
sd_19_map_chars = MODULE.sd_19_map_chars
sd_20_encode_cipher_map = MODULE.sd_20_encode_cipher_map
sd_21_invert_dict = MODULE.sd_21_invert_dict
sd_22_merge_dicts_sum = MODULE.sd_22_merge_dicts_sum
sd_23_dict_filter_threshold = MODULE.sd_23_dict_filter_threshold
sd_24_dict_argmax_value = MODULE.sd_24_dict_argmax_value
sd_25_histogram_even_odd = MODULE.sd_25_histogram_even_odd
sd_26_longest_palindromic_substring_simple = MODULE.sd_26_longest_palindromic_substring_simple
sd_27_longest_common_prefix = MODULE.sd_27_longest_common_prefix
sd_28_word_pattern = MODULE.sd_28_word_pattern
sd_29_decode_run_length_str = MODULE.sd_29_decode_run_length_str
sd_30_letter_combinations_phone = MODULE.sd_30_letter_combinations_phone


def test_basic_string_scans():
    assert sd_01_count_vowels("abc") == 1
    assert sd_01_count_vowels("XYZ") == 0
    assert sd_02_count_substring_overlap("aaaa", "aa") == 3
    assert sd_02_count_substring_overlap("abc", "x") == 0
    assert sd_03_reverse_string("abc") == "cba"
    assert sd_03_reverse_string("") == ""
    assert sd_04_is_palindrome("racecar") is True
    assert sd_04_is_palindrome("abc") is False
    assert sd_05_only_alpha_lower("A1b*C") == "abc"
    assert sd_05_only_alpha_lower("123") == ""


def test_parsing_and_tokenization():
    assert sd_06_split_on_spaces("a b  c") == ["a", "b", "c"]
    assert sd_06_split_on_spaces("") == []
    assert sd_07_join_with_comma(["a", "b", "c"]) == "a,b,c"
    assert sd_07_join_with_comma([]) == ""
    assert sd_08_strip_outer_spaces("  abc  ") == "abc"
    assert sd_08_strip_outer_spaces("abc") == "abc"
    assert sd_09_normalize_whitespace("  a   b  c ") == "a b c"
    assert sd_10_extract_digits("a1b23c") == "123"
    assert sd_10_extract_digits("") == ""


def test_frequency_and_grouping():
    assert sd_11_char_frequency("aba") == {"a": 2, "b": 1}
    assert sd_11_char_frequency("") == {}
    assert sd_12_word_frequency("a b a c a") == {"a": 3, "b": 1, "c": 1}
    assert sd_13_most_frequent_char("bbaac") == "a"
    assert sd_13_most_frequent_char("") is None
    assert sd_14_anagram_dict(["eat", "tea", "tan", "ate", "nat", "bat"]) == {
        "aet": ["eat", "tea", "ate"],
        "ant": ["tan", "nat"],
        "abt": ["bat"],
    }
    assert sd_15_group_words_by_length(["a", "to", "hi", "x"]) == {1: ["a", "x"], 2: ["to", "hi"]}


def test_combined_algorithms():
    assert sd_16_is_anagram("listen", "silent") is True
    assert sd_16_is_anagram("abc", "abz") is False
    assert sd_17_first_unique_char("aabbcd") == "c"
    assert sd_17_first_unique_char("aabb") is None
    assert sd_18_replace_words_dict(["a", "b", "c"], {"b": "beta"}) == ["a", "beta", "c"]
    assert sd_19_map_chars("abc", {"a": "1", "c": "9"}) == "1b9"
    assert sd_20_encode_cipher_map("abca", {"a": "x", "c": "y"}) == "xbyx"


def test_dict_search_and_histogram():
    assert sd_21_invert_dict({"a": 1, "b": 2, "c": 1}) == {1: ["a", "c"], 2: ["b"]}
    assert sd_22_merge_dicts_sum({"x": 1, "y": 2}, {"y": 5, "z": 3}) == {"x": 1, "y": 7, "z": 3}
    assert sd_23_dict_filter_threshold({"a": 2, "b": 5, "c": 1}, 2) == {"a": 2, "b": 5}
    assert sd_24_dict_argmax_value({"a": 3, "b": 3, "c": 2}) == "a"
    assert sd_24_dict_argmax_value({}) is None
    assert sd_25_histogram_even_odd([1, 2, 3, 4]) == {"even": 2, "odd": 2}


def test_challenge_problems():
    assert sd_26_longest_palindromic_substring_simple("babad") in ["bab", "aba"]
    assert sd_26_longest_palindromic_substring_simple("cbbd") == "bb"
    assert sd_27_longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert sd_27_longest_common_prefix([]) == ""
    assert sd_28_word_pattern("abba", "dog cat cat dog") is True
    assert sd_28_word_pattern("abba", "dog cat cat fish") is False
    assert sd_29_decode_run_length_str("a3b1c2") == "aaabcc"
    assert sd_29_decode_run_length_str("") == ""
    with pytest.raises(ValueError):
        sd_29_decode_run_length_str("abc")
    combos = sd_30_letter_combinations_phone("23")
    assert sorted(combos) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sd_30_letter_combinations_phone("") == []

