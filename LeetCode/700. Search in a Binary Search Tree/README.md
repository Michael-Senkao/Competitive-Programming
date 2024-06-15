# [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree)

You are given the <code>root</code> of a binary search tree (BST) and an integer <code>val</code>.

Find the node in the BST that the node's value equals <code>val</code> and return the subtree rooted with that node. If such a node 
does not exist, return <code>null</code>.

### **Example 1:**
<img src="https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg" />
<pre>
<strong>Input:</strong> root = [4,2,7,1,3], val = 2
<strong>Output:</strong> [2,1,3]
</pre>

### **Example 2:**
<img src="https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg" />
<pre>
<strong>Input:</strong> root = [4,2,7,1,3], val = 5
<strong>Output:</strong> []
</pre>

### **Constraints:**

- The number of nodes in the tree is in the range <code>[1, 5000]</code>.
- <code> 1 <= Node.val <= 10<sup>7</sup></code>
- <code>root</code> is a binary search tree.
- <code>1 <= val <= 10<sup>7</sup></code>
