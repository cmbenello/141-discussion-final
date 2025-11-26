from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TreeNode:
    value: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"]
    is_word: bool = False


def tt_01_tree_size(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + tt_01_tree_size(root.left) + tt_01_tree_size(root.right)


def tt_02_tree_height(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(tt_02_tree_height(root.left), tt_02_tree_height(root.right))


def tt_03_count_leaves(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return tt_03_count_leaves(root.left) + tt_03_count_leaves(root.right)


def tt_04_count_internal_nodes(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + tt_04_count_internal_nodes(root.left) + tt_04_count_internal_nodes(root.right)


def tt_05_tree_sum(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return root.value + tt_05_tree_sum(root.left) + tt_05_tree_sum(root.right)


def tt_06_tree_min(root: Optional[TreeNode]) -> Optional[int]:
    if root is None:
        return None
    vals = [root.value]
    left_min = tt_06_tree_min(root.left)
    right_min = tt_06_tree_min(root.right)
    if left_min is not None:
        vals.append(left_min)
    if right_min is not None:
        vals.append(right_min)
    return min(vals)


def tt_07_tree_max(root: Optional[TreeNode]) -> Optional[int]:
    if root is None:
        return None
    vals = [root.value]
    left_max = tt_07_tree_max(root.left)
    right_max = tt_07_tree_max(root.right)
    if left_max is not None:
        vals.append(left_max)
    if right_max is not None:
        vals.append(right_max)
    return max(vals)


def tt_08_contains_value(root: Optional[TreeNode], target: int) -> bool:
    if root is None:
        return False
    if root.value == target:
        return True
    return tt_08_contains_value(root.left, target) or tt_08_contains_value(root.right, target)


def tt_09_count_value(root: Optional[TreeNode], target: int) -> int:
    if root is None:
        return 0
    return (1 if root.value == target else 0) + tt_09_count_value(root.left, target) + tt_09_count_value(
        root.right, target
    )


def tt_10_is_singleton(root: Optional[TreeNode]) -> bool:
    if root is None:
        return False
    return root.left is None and root.right is None


def tt_11_preorder(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return [root.value] + tt_11_preorder(root.left) + tt_11_preorder(root.right)


def tt_12_inorder(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return tt_12_inorder(root.left) + [root.value] + tt_12_inorder(root.right)


def tt_13_postorder(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return tt_13_postorder(root.left) + tt_13_postorder(root.right) + [root.value]


def tt_14_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    result: List[List[int]] = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level: List[int] = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def tt_15_tree_to_nested_list(root: Optional[TreeNode]) -> Optional[List[Any]]:
    if root is None:
        return None
    return [root.value, tt_15_tree_to_nested_list(root.left), tt_15_tree_to_nested_list(root.right)]


def tt_16_mirror_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    return TreeNode(root.value, tt_16_mirror_tree(root.right), tt_16_mirror_tree(root.left))


def tt_17_same_shape(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None or b is None:
        return a is b
    return tt_17_same_shape(a.left, b.left) and tt_17_same_shape(a.right, b.right)


def tt_18_is_symmetric(root: Optional[TreeNode]) -> bool:
    def mirror(l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if l is None or r is None:
            return l is r
        return l.value == r.value and mirror(l.left, r.right) and mirror(l.right, r.left)

    if root is None:
        return True
    return mirror(root.left, root.right)


def tt_19_max_level_sum(root: Optional[TreeNode]) -> int:
    levels = tt_14_level_order(root)
    return max((sum(level) for level in levels), default=0)


def tt_20_left_view(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    view: List[int] = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:
                view.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return view


def tt_21_is_bst_strict(root: Optional[TreeNode]) -> bool:
    def helper(node: Optional[TreeNode], low: Optional[int], high: Optional[int]) -> bool:
        if node is None:
            return True
        if (low is not None and node.value <= low) or (high is not None and node.value >= high):
            return False
        return helper(node.left, low, node.value) and helper(node.right, node.value, high)

    return helper(root, None, None)


def tt_22_bst_search(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if root is None:
        return None
    if target == root.value:
        return root
    if target < root.value:
        return tt_22_bst_search(root.left, target)
    return tt_22_bst_search(root.right, target)


def tt_23_bst_insert(root: Optional[TreeNode], value: int) -> TreeNode:
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = tt_23_bst_insert(root.left, value)
    elif value > root.value:
        root.right = tt_23_bst_insert(root.right, value)
    return root


def tt_24_bst_find_min(root: Optional[TreeNode]) -> Optional[int]:
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.value


def tt_25_bst_find_max(root: Optional[TreeNode]) -> Optional[int]:
    if root is None:
        return None
    current = root
    while current.right:
        current = current.right
    return current.value


def tt_26_bst_floor(root: Optional[TreeNode], target: int) -> Optional[int]:
    floor_val: Optional[int] = None
    current = root
    while current:
        if current.value == target:
            return current.value
        if current.value < target:
            floor_val = current.value
            current = current.right
        else:
            current = current.left
    return floor_val


def tt_27_bst_ceiling(root: Optional[TreeNode], target: int) -> Optional[int]:
    ceil_val: Optional[int] = None
    current = root
    while current:
        if current.value == target:
            return current.value
        if current.value > target:
            ceil_val = current.value
            current = current.left
        else:
            current = current.right
    return ceil_val


def tt_28_bst_inorder_successor(root: Optional[TreeNode], target: int) -> Optional[int]:
    successor: Optional[int] = None
    current = root
    while current:
        if target < current.value:
            successor = current.value
            current = current.left
        elif target > current.value:
            current = current.right
        else:
            if current.right:
                succ_node = current.right
                while succ_node.left:
                    succ_node = succ_node.left
                successor = succ_node.value
            break
    return successor


def tt_29_bst_range_sum(root: Optional[TreeNode], low: int, high: int) -> int:
    if root is None:
        return 0
    total = 0
    if low <= root.value <= high:
        total += root.value
    if root.value > low:
        total += tt_29_bst_range_sum(root.left, low, high)
    if root.value < high:
        total += tt_29_bst_range_sum(root.right, low, high)
    return total


def tt_30_bst_kth_smallest(root: Optional[TreeNode], k: int) -> Optional[int]:
    stack: List[TreeNode] = []
    current = root
    count = 0
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        count += 1
        if count == k:
            return current.value
        current = current.right
    return None


def tt_31_root_to_leaf_paths(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [[root.value]]
    paths: List[List[int]] = []
    for child in (root.left, root.right):
        for path in tt_31_root_to_leaf_paths(child):
            paths.append([root.value] + path)
    return paths


def tt_32_has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if root is None:
        return False
    remaining = target_sum - root.value
    if root.left is None and root.right is None:
        return remaining == 0
    return tt_32_has_path_sum(root.left, remaining) or tt_32_has_path_sum(root.right, remaining)


def tt_33_all_path_sums(root: Optional[TreeNode]) -> List[int]:
    sums: List[int] = []
    for path in tt_31_root_to_leaf_paths(root):
        sums.append(sum(path))
    return sums


def tt_34_longest_root_to_leaf_length(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(tt_34_longest_root_to_leaf_length(root.left), tt_34_longest_root_to_leaf_length(root.right))


def tt_35_diameter(root: Optional[TreeNode]) -> int:
    diameter = 0

    def height(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if node is None:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)
        diameter = max(diameter, left_h + right_h + 1)
        return 1 + max(left_h, right_h)

    height(root)
    return diameter


def tt_36_max_root_to_leaf_sum(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.value
    left_sum = tt_36_max_root_to_leaf_sum(root.left)
    right_sum = tt_36_max_root_to_leaf_sum(root.right)
    return root.value + max(left_sum, right_sum)


def tt_37_count_paths_target_sum(root: Optional[TreeNode], target: int) -> int:
    count = 0

    def dfs(node: Optional[TreeNode], path_sums: List[int]) -> None:
        nonlocal count
        if node is None:
            return
        new_sums = [node.value + s for s in path_sums] + [node.value]
        count += sum(1 for s in new_sums if s == target)
        dfs(node.left, new_sums)
        dfs(node.right, new_sums)

    dfs(root, [])
    return count


def tt_38_lowest_common_ancestor(root: Optional[TreeNode], a: int, b: int) -> Optional[int]:
    def helper(node: Optional[TreeNode]) -> Tuple[bool, bool, Optional[int]]:
        if node is None:
            return False, False, None
        left_found_a, left_found_b, left_lca = helper(node.left)
        right_found_a, right_found_b, right_lca = helper(node.right)
        if left_lca is not None:
            return True, True, left_lca
        if right_lca is not None:
            return True, True, right_lca
        found_a = left_found_a or right_found_a or node.value == a
        found_b = left_found_b or right_found_b or node.value == b
        if found_a and found_b:
            return True, True, node.value
        return found_a, found_b, None

    _, _, lca = helper(root)
    return lca


def tt_39_are_cousins(root: Optional[TreeNode], a: int, b: int) -> bool:
    if root is None:
        return False
    queue = deque([(root, None)])
    while queue:
        level_size = len(queue)
        parent_a = parent_b = None
        for _ in range(level_size):
            node, parent = queue.popleft()
            if node.value == a:
                parent_a = parent
            if node.value == b:
                parent_b = parent
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        if parent_a or parent_b:
            return parent_a is not None and parent_b is not None and parent_a != parent_b
    return False


def tt_40_prune_below_threshold(root: Optional[TreeNode], threshold: int) -> Optional[TreeNode]:
    if root is None:
        return None
    left = tt_40_prune_below_threshold(root.left, threshold)
    right = tt_40_prune_below_threshold(root.right, threshold)
    if left is None and right is None and root.value < threshold:
        return None
    return TreeNode(root.value, left, right)


def tt_41_trie_insert(root: TrieNode, word: str) -> None:
    node = root
    for ch in word:
        if ch not in node.children:
            node.children[ch] = TrieNode(children={})
        node = node.children[ch]
    node.is_word = True


def tt_42_trie_contains(root: TrieNode, word: str) -> bool:
    node = root
    for ch in word:
        if ch not in node.children:
            return False
        node = node.children[ch]
    return node.is_word


def tt_43_trie_is_prefix(root: TrieNode, prefix: str) -> bool:
    node = root
    for ch in prefix:
        if ch not in node.children:
            return False
        node = node.children[ch]
    return True


def tt_44_trie_words_with_prefix(root: TrieNode, prefix: str) -> List[str]:
    results: List[str] = []
    node = root
    for ch in prefix:
        if ch not in node.children:
            return []
        node = node.children[ch]

    def dfs(n: TrieNode, path: List[str]) -> None:
        if n.is_word:
            results.append(prefix + "".join(path))
        for ch, child in n.children.items():
            path.append(ch)
            dfs(child, path)
            path.pop()

    dfs(node, [])
    return results


def tt_45_trie_count_words(root: TrieNode) -> int:
    count = 1 if root.is_word else 0
    for child in root.children.values():
        count += tt_45_trie_count_words(child)
    return count


def tt_46_trie_longest_prefix_of(root: TrieNode, s: str) -> str:
    node = root
    longest = 0
    for i, ch in enumerate(s):
        if ch not in node.children:
            break
        node = node.children[ch]
        if node.is_word:
            longest = i + 1
    return s[:longest]


def tt_47_trie_collect_words(root: TrieNode) -> List[str]:
    words: List[str] = []

    def dfs(node: TrieNode, path: List[str]) -> None:
        if node.is_word:
            words.append("".join(path))
        for ch, child in node.children.items():
            path.append(ch)
            dfs(child, path)
            path.pop()

    dfs(root, [])
    return words


def tt_48_trie_delete_word_shallow(root: TrieNode, word: str) -> None:
    node = root
    for ch in word:
        if ch not in node.children:
            return
        node = node.children[ch]
    node.is_word = False


def tt_49_trie_autocomplete_k(root: TrieNode, prefix: str, k: int) -> List[str]:
    if k <= 0:
        return []
    words = tt_44_trie_words_with_prefix(root, prefix)
    return words[:k]


def tt_50_trie_is_complete_for_alphabet(root: TrieNode, alphabet: List[str]) -> bool:
    for letter in alphabet:
        if not tt_43_trie_is_prefix(root, letter):
            return False
    return True
