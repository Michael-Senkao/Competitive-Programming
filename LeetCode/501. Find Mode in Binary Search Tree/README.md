# [501. Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree)

Given the <code>root</code> of a binary search tree (BST) with duplicates, return <em>all the [mode(s)](https://en.wikipedia.org/wiki/Mode_(statistics)) 
(i.e., the most frequently occurred element) in it</em>.

If the tree has more than one mode, return them in <strong>any order</strong>.

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys <strong>less than or equal to</strong> the node's key.
- The right subtree of a node contains only nodes with keys <strong>greater than or equal to</strong> the node's key.
- Both the left and right subtrees must also be binary search trees.

  ### **Example 1:**
  <img src = "https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg" />
  <pre>
    <strong>Input:</strong> root = [1,null,2,2]
    <strong>Output:</strong> [2]
  </pre>
### **Example 2:**
  <pre>
    <strong>Input:</strong> root = root = [0]
    <strong>Output:</strong> [0]
  </pre>

### **Constraints:**

- The number of nodes in the tree is in the range <code>[1, 104]</code>.
- <code>-105 <= Node.val <= 105</code>
