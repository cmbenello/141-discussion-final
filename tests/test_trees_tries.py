from __future__ import annotations

import importlib
import os

import pytest


USE_SOLUTIONS = os.getenv("USE_SOLUTIONS") == "1"
MODULE = importlib.import_module(
    "solutions.trees_tries_sols" if USE_SOLUTIONS else "problems.trees_tries"
)

TreeNode = MODULE.TreeNode
TrieNode = MODULE.TrieNode
tt_01_tree_size = MODULE.tt_01_tree_size
tt_02_tree_height = MODULE.tt_02_tree_height
tt_03_count_leaves = MODULE.tt_03_count_leaves
tt_04_count_internal_nodes = MODULE.tt_04_count_internal_nodes
tt_05_tree_sum = MODULE.tt_05_tree_sum
tt_06_tree_min = MODULE.tt_06_tree_min
tt_07_tree_max = MODULE.tt_07_tree_max
tt_08_contains_value = MODULE.tt_08_contains_value
tt_09_count_value = MODULE.tt_09_count_value
tt_10_is_singleton = MODULE.tt_10_is_singleton
tt_11_preorder = MODULE.tt_11_preorder
tt_12_inorder = MODULE.tt_12_inorder
tt_13_postorder = MODULE.tt_13_postorder
tt_14_level_order = MODULE.tt_14_level_order
tt_15_tree_to_nested_list = MODULE.tt_15_tree_to_nested_list
tt_16_mirror_tree = MODULE.tt_16_mirror_tree
tt_17_same_shape = MODULE.tt_17_same_shape
tt_18_is_symmetric = MODULE.tt_18_is_symmetric
tt_19_max_level_sum = MODULE.tt_19_max_level_sum
tt_20_left_view = MODULE.tt_20_left_view
tt_21_is_bst_strict = MODULE.tt_21_is_bst_strict
tt_22_bst_search = MODULE.tt_22_bst_search
tt_23_bst_insert = MODULE.tt_23_bst_insert
tt_24_bst_find_min = MODULE.tt_24_bst_find_min
tt_25_bst_find_max = MODULE.tt_25_bst_find_max
tt_26_bst_floor = MODULE.tt_26_bst_floor
tt_27_bst_ceiling = MODULE.tt_27_bst_ceiling
tt_28_bst_inorder_successor = MODULE.tt_28_bst_inorder_successor
tt_29_bst_range_sum = MODULE.tt_29_bst_range_sum
tt_30_bst_kth_smallest = MODULE.tt_30_bst_kth_smallest
tt_31_root_to_leaf_paths = MODULE.tt_31_root_to_leaf_paths
tt_32_has_path_sum = MODULE.tt_32_has_path_sum
tt_33_all_path_sums = MODULE.tt_33_all_path_sums
tt_34_longest_root_to_leaf_length = MODULE.tt_34_longest_root_to_leaf_length
tt_35_diameter = MODULE.tt_35_diameter
tt_36_max_root_to_leaf_sum = MODULE.tt_36_max_root_to_leaf_sum
tt_37_count_paths_target_sum = MODULE.tt_37_count_paths_target_sum
tt_38_lowest_common_ancestor = MODULE.tt_38_lowest_common_ancestor
tt_39_are_cousins = MODULE.tt_39_are_cousins
tt_40_prune_below_threshold = MODULE.tt_40_prune_below_threshold
tt_41_trie_insert = MODULE.tt_41_trie_insert
tt_42_trie_contains = MODULE.tt_42_trie_contains
tt_43_trie_is_prefix = MODULE.tt_43_trie_is_prefix
tt_44_trie_words_with_prefix = MODULE.tt_44_trie_words_with_prefix
tt_45_trie_count_words = MODULE.tt_45_trie_count_words
tt_46_trie_longest_prefix_of = MODULE.tt_46_trie_longest_prefix_of
tt_47_trie_collect_words = MODULE.tt_47_trie_collect_words
tt_48_trie_delete_word_shallow = MODULE.tt_48_trie_delete_word_shallow
tt_49_trie_autocomplete_k = MODULE.tt_49_trie_autocomplete_k
tt_50_trie_is_complete_for_alphabet = MODULE.tt_50_trie_is_complete_for_alphabet


def _sample_tree() -> TreeNode:
    return TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))


def test_basic_tree_properties():
    empty = None
    assert tt_01_tree_size(empty) == 0
    assert tt_02_tree_height(empty) == 0
    t = TreeNode(1, TreeNode(2), TreeNode(3))
    assert tt_01_tree_size(t) == 3
    assert tt_02_tree_height(t) == 2
    assert tt_03_count_leaves(t) == 2
    assert tt_04_count_internal_nodes(t) == 1
    assert tt_05_tree_sum(t) == 6
    assert tt_06_tree_min(t) == 1
    assert tt_07_tree_max(t) == 3
    assert tt_08_contains_value(t, 2) is True
    assert tt_08_contains_value(t, 9) is False
    assert tt_09_count_value(TreeNode(1, TreeNode(1), TreeNode(2)), 1) == 2
    assert tt_10_is_singleton(TreeNode(5)) is True
    assert tt_10_is_singleton(TreeNode(5, TreeNode(6))) is False


def test_traversals_and_views():
    t = _sample_tree()
    assert tt_11_preorder(t) == [1, 2, 4, 5, 3]
    assert tt_12_inorder(t) == [4, 2, 5, 1, 3]
    assert tt_13_postorder(t) == [4, 5, 2, 3, 1]
    assert tt_14_level_order(t) == [[1], [2, 3], [4, 5]]
    assert tt_15_tree_to_nested_list(t) == [1, [2, [4, None, None], [5, None, None]], [3, None, None]]
    mirrored = tt_16_mirror_tree(t)
    assert tt_12_inorder(mirrored) == [3, 1, 5, 2, 4]
    t1 = TreeNode(1, TreeNode(2), None)
    t2 = TreeNode(9, TreeNode(8), None)
    assert tt_17_same_shape(t1, t2) is True
    assert tt_17_same_shape(t1, TreeNode(1, None, TreeNode(2))) is False
    sym = TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, None, TreeNode(3)))
    assert tt_18_is_symmetric(sym) is True
    assert tt_19_max_level_sum(TreeNode(1, TreeNode(7), TreeNode(0))) == 7
    left_view_tree = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, None, TreeNode(5)))
    assert tt_20_left_view(left_view_tree) == [1, 2, 4]


def test_bst_operations():
    t = TreeNode(2, TreeNode(1), TreeNode(3))
    assert tt_21_is_bst_strict(t) is True
    bad = TreeNode(2, TreeNode(3), TreeNode(1))
    assert tt_21_is_bst_strict(bad) is False
    assert tt_22_bst_search(t, 3).value == 3
    assert tt_22_bst_search(t, 9) is None
    root = None
    for v in [5, 3, 7, 6]:
        root = tt_23_bst_insert(root, v)
    assert tt_12_inorder(root) == [3, 5, 6, 7]
    assert tt_24_bst_find_min(root) == 3
    assert tt_25_bst_find_max(root) == 7
    floor_tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8))
    assert tt_26_bst_floor(floor_tree, 4) == 4
    assert tt_26_bst_floor(floor_tree, 1) is None
    assert tt_27_bst_ceiling(floor_tree, 4) == 4
    assert tt_27_bst_ceiling(floor_tree, 9) is None
    succ_tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8, None, TreeNode(10)))
    assert tt_28_bst_inorder_successor(succ_tree, 4) == 5
    assert tt_28_bst_inorder_successor(succ_tree, 10) is None
    range_tree = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
    assert tt_29_bst_range_sum(range_tree, 7, 15) == 32
    assert tt_30_bst_kth_smallest(range_tree, 3) == 7
    assert tt_30_bst_kth_smallest(range_tree, 20) is None


def test_path_based_and_aggregate():
    t = _sample_tree()
    assert sorted(tt_31_root_to_leaf_paths(t)) == [[1, 2, 4], [1, 2, 5], [1, 3]]
    assert tt_32_has_path_sum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8)), 22)
    assert sorted(tt_33_all_path_sums(t)) == [4, 7, 8]
    assert tt_34_longest_root_to_leaf_length(t) == 3
    assert tt_35_diameter(t) == 4
    assert tt_36_max_root_to_leaf_sum(TreeNode(1, TreeNode(2), TreeNode(3))) == 4
    count_tree = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(2)), TreeNode(-3, None, TreeNode(11)))
    assert tt_37_count_paths_target_sum(count_tree, 8) == 2
    lca_tree = TreeNode(
        3,
        TreeNode(5, TreeNode(6), TreeNode(2)),
        TreeNode(1, TreeNode(0), TreeNode(8)),
    )
    assert tt_38_lowest_common_ancestor(lca_tree, 6, 2) == 5
    cousins_tree = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, None, TreeNode(5)))
    assert tt_39_are_cousins(cousins_tree, 4, 5) is True
    prune_tree = TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(3), TreeNode(9)))
    pruned = tt_40_prune_below_threshold(prune_tree, 4)
    assert tt_11_preorder(pruned) == [5, 7, 9]


def test_tries():
    root = TrieNode(children={})
    tt_41_trie_insert(root, "cat")
    tt_41_trie_insert(root, "car")
    tt_41_trie_insert(root, "dog")
    assert tt_42_trie_contains(root, "cat") is True
    assert tt_42_trie_contains(root, "cow") is False
    assert tt_43_trie_is_prefix(root, "ca") is True
    assert tt_43_trie_is_prefix(root, "do") is True
    assert tt_43_trie_is_prefix(root, "z") is False
    words_with_ca = tt_44_trie_words_with_prefix(root, "ca")
    assert set(words_with_ca) == {"cat", "car"}
    assert tt_45_trie_count_words(root) == 3
    assert tt_46_trie_longest_prefix_of(root, "cattle") == "cat"
    assert tt_46_trie_longest_prefix_of(root, "zoo") == ""
    collected = tt_47_trie_collect_words(root)
    assert set(collected) == {"cat", "car", "dog"}
    tt_48_trie_delete_word_shallow(root, "car")
    assert tt_42_trie_contains(root, "car") is False
    auto = tt_49_trie_autocomplete_k(root, "ca", 2)
    assert len(auto) <= 2 and all(w.startswith("ca") for w in auto)
    assert tt_50_trie_is_complete_for_alphabet(root, ["c", "d"]) is True
    assert tt_50_trie_is_complete_for_alphabet(root, ["c", "e"]) is False
