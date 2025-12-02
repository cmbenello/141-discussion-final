from __future__ import annotations

"""
Test collection helpers that let you filter by problem/function name.

Some test files group many problems into a single test function (e.g., all
recursion basics live inside test_basic_structural_recursion). By adding custom
keywords to those items during collection, `pytest -k "<function_name>"` will
match the grouped test and let you run a single problem's checks.
"""

from typing import Dict, List

import pytest
from pytest import hookimpl

# Mapping from collected test nodeid to the problem/function keywords it covers.
FUNCTION_KEYWORDS: Dict[str, List[str]] = {
    # basics.py
    "tests/test_basics.py::test_basic_expressions_and_types": [
        "ba_01_add_three",
        "ba_02_safe_int_div",
        "ba_03_average_ignore_none",
        "ba_04_clamp",
        "ba_05_quadratic_eval",
        "ba_06_is_close",
        "ba_07_to_bool_list",
        "ba_08_parse_rgb_hex",
        "ba_09_seconds_to_hms",
        "ba_10_hms_to_seconds",
    ],
    "tests/test_basics.py::test_lists_and_tuples": [
        "ba_11_first_last",
        "ba_12_rotate_right",
        "ba_13_remove_negatives_in_place",
        "ba_14_dedup_preserve_order",
        "ba_15_pairwise_sums",
        "ba_16_split_by_parity",
        "ba_17_chunk_list",
        "ba_18_argmax",
        "ba_19_all_prefix_sums",
        "ba_20_interleave_lists",
    ],
    "tests/test_basics.py::test_functions_and_mutability": [
        "ba_21_increment_all_in_place",
        "ba_22_increment_copy",
        "ba_23_append_log",
        "ba_24_copy_and_append",
        "ba_25_update_counter",
        "ba_26_clone_and_update_counter",
        "ba_27_safe_pop",
        "ba_28_zero_out_below_threshold",
        "ba_29_extend_if_short",
        "ba_30_normalize_scores",
    ],
    "tests/test_basics.py::test_point2d": ["Point2D"],
    "tests/test_basics.py::test_bankaccount": ["BankAccount"],
    "tests/test_basics.py::test_todolist": ["TodoList"],
    # strings_dicts.py
    "tests/test_strings_dicts.py::test_basic_string_scans": [
        "sd_01_count_vowels",
        "sd_02_count_substring_overlap",
        "sd_03_reverse_string",
        "sd_04_is_palindrome",
        "sd_05_only_alpha_lower",
    ],
    "tests/test_strings_dicts.py::test_parsing_and_tokenization": [
        "sd_06_split_on_spaces",
        "sd_07_join_with_comma",
        "sd_08_strip_outer_spaces",
        "sd_09_normalize_whitespace",
        "sd_10_extract_digits",
    ],
    "tests/test_strings_dicts.py::test_frequency_and_grouping": [
        "sd_11_char_frequency",
        "sd_12_word_frequency",
        "sd_13_most_frequent_char",
        "sd_14_anagram_dict",
        "sd_15_group_words_by_length",
    ],
    "tests/test_strings_dicts.py::test_combined_algorithms": [
        "sd_16_is_anagram",
        "sd_17_first_unique_char",
        "sd_18_replace_words_dict",
        "sd_19_map_chars",
        "sd_20_encode_cipher_map",
    ],
    "tests/test_strings_dicts.py::test_dict_search_and_histogram": [
        "sd_21_invert_dict",
        "sd_22_merge_dicts_sum",
        "sd_23_dict_filter_threshold",
        "sd_24_dict_argmax_value",
        "sd_25_histogram_even_odd",
    ],
    "tests/test_strings_dicts.py::test_challenge_problems": [
        "sd_26_longest_palindromic_substring_simple",
        "sd_27_longest_common_prefix",
        "sd_28_word_pattern",
        "sd_29_decode_run_length_str",
        "sd_30_letter_combinations_phone",
    ],
    # recursion_lists.py
    "tests/test_recursion_lists.py::test_basic_structural_recursion": [
        "rl_01_len_recursive",
        "rl_02_sum_recursive",
        "rl_03_count_occurrences",
        "rl_04_contains",
        "rl_05_all_positive",
        "rl_06_any_negative",
        "rl_07_max_recursive",
        "rl_08_min_recursive",
        "rl_09_index_of_first",
        "rl_10_index_of_last",
    ],
    "tests/test_recursion_lists.py::test_recursive_transformations": [
        "rl_11_copy_list",
        "rl_12_reverse_new",
        "rl_13_increment_all",
        "rl_14_filter_even",
        "rl_15_remove_target",
        "rl_16_take_first_n",
        "rl_17_drop_first_n",
        "rl_18_concat_lists",
        "rl_19_interleave_recursive",
        "rl_20_flatten_shallow",
    ],
    "tests/test_recursion_lists.py::test_divide_and_conquer_lists": [
        "rl_21_binary_search_recursive",
        "rl_22_merge_two_sorted_recursive",
        "rl_23_merge_sort_recursive",
        "rl_24_is_sorted_recursive",
        "rl_25_count_inversions_simple",
        "rl_26_count_smaller_to_right",
        "rl_27_max_subarray_sum_simple",
        "rl_28_split_even_odd_indices",
        "rl_29_find_min_max_recursive",
        "rl_30_rotate_left_recursive",
    ],
    "tests/test_recursion_lists.py::test_two_sided_recursion_helpers": [
        "rl_31_len_from_index",
        "rl_32_sum_from_index",
        "rl_33_is_palindrome_list",
        "rl_34_lists_equal",
        "rl_35_zip_lists_recursive",
        "rl_36_unzip_pairs_recursive",
        "rl_37_all_prefixes",
        "rl_38_all_suffixes",
        "rl_39_split_at_index",
        "rl_40_run_length_encode_recursive",
    ],
    "tests/test_recursion_lists.py::test_nested_structures": [
        "rl_41_total_length_nested",
        "rl_42_sum_nested_ints",
        "rl_43_flatten_nested",
        "rl_44_max_depth_nested",
        "rl_45_contains_in_nested",
    ],
    "tests/test_recursion_lists.py::test_backtracking_combinatorial": [
        "rl_46_subsets_all",
        "rl_47_permutations_all",
        "rl_48_can_reach_sum_by_signs",
        "rl_49_split_into_two_equal_sum",
        "rl_50_all_ways_to_split_into_runs",
    ],
    # trees_tries.py
    "tests/test_trees_tries.py::test_basic_tree_properties": [
        "tt_01_tree_size",
        "tt_02_tree_height",
        "tt_03_count_leaves",
        "tt_04_count_internal_nodes",
        "tt_05_tree_sum",
        "tt_06_tree_min",
        "tt_07_tree_max",
        "tt_08_contains_value",
        "tt_09_count_value",
        "tt_10_is_singleton",
    ],
    "tests/test_trees_tries.py::test_traversals_and_views": [
        "tt_11_preorder",
        "tt_12_inorder",
        "tt_13_postorder",
        "tt_14_level_order",
        "tt_15_tree_to_nested_list",
        "tt_16_mirror_tree",
        "tt_17_same_shape",
        "tt_18_is_symmetric",
        "tt_19_max_level_sum",
        "tt_20_left_view",
    ],
    "tests/test_trees_tries.py::test_bst_operations": [
        "tt_21_is_bst_strict",
        "tt_22_bst_search",
        "tt_23_bst_insert",
        "tt_24_bst_find_min",
        "tt_25_bst_find_max",
        "tt_26_bst_floor",
        "tt_27_bst_ceiling",
        "tt_28_bst_inorder_successor",
        "tt_29_bst_range_sum",
        "tt_30_bst_kth_smallest",
    ],
    "tests/test_trees_tries.py::test_path_based_and_aggregate": [
        "tt_31_root_to_leaf_paths",
        "tt_32_has_path_sum",
        "tt_33_all_path_sums",
        "tt_34_longest_root_to_leaf_length",
        "tt_35_diameter",
        "tt_36_max_root_to_leaf_sum",
        "tt_37_count_paths_target_sum",
        "tt_38_lowest_common_ancestor",
        "tt_39_are_cousins",
        "tt_40_prune_below_threshold",
    ],
    "tests/test_trees_tries.py::test_tries": [
        "tt_41_trie_insert",
        "tt_42_trie_contains",
        "tt_43_trie_is_prefix",
        "tt_44_trie_words_with_prefix",
        "tt_45_trie_count_words",
        "tt_46_trie_longest_prefix_of",
        "tt_47_trie_collect_words",
        "tt_48_trie_delete_word_shallow",
        "tt_49_trie_autocomplete_k",
        "tt_50_trie_is_complete_for_alphabet",
    ],
}


def _flatten_targets(raw_targets: List[str]) -> set[str]:
    targets: set[str] = set()
    for raw in raw_targets:
        for part in raw.split(","):
            part = part.strip()
            if part:
                targets.add(part)
    return targets


def _add_keywords(item: pytest.Item) -> None:
    for kw in FUNCTION_KEYWORDS.get(item.nodeid, []):
        item.keywords[kw] = True
        # Make keywords visible to -k substring matching (uses extra_keyword_matches).
        item.extra_keyword_matches.add(kw)


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--problem",
        action="append",
        default=[],
        help="Run only tests covering the given problem/function name(s). "
        "Accepts comma-separated values and can be repeated.",
    )


@hookimpl(tryfirst=True)
def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    # Attach keywords for convenience (helps readability and any downstream filters).
    for item in items:
        _add_keywords(item)

    targets = _flatten_targets(config.getoption("--problem"))
    if not targets:
        return

    selected: list[pytest.Item] = []
    deselected: list[pytest.Item] = []
    lowered_targets = {t.lower() for t in targets}

    for item in items:
        item_keywords = set(FUNCTION_KEYWORDS.get(item.nodeid, []))
        item_keywords.add(item.name)
        keyword_lowers = {kw.lower() for kw in item_keywords}
        nodeid_lower = item.nodeid.lower()

        # Match if any target is explicitly mapped to this item or is a substring of the nodeid.
        if any(
            target in keyword_lowers or target in nodeid_lower
            for target in lowered_targets
        ):
            selected.append(item)
        else:
            deselected.append(item)

    if deselected:
        config.hook.pytest_deselected(items=deselected)
    items[:] = selected


def pytest_itemcollected(item: pytest.Item) -> None:
    """Ensure keywords are available as soon as an item is created (helps -k)."""
    _add_keywords(item)
