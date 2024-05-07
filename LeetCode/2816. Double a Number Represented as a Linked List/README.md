<h2> <a href = "https://leetcode.com/problems/double-a-number-represented-as-a-linked-list"> 2816. Double a Number Represented as a Linked List</a></h2>

You are given the <code>head</code> of a <strong>non-empty</strong> linked list representing a non-negative integer without leading zeroes.

<em>Return the</em> <code>head</code> <em>of the linked list after <strong>doubling</strong> it</em>.

 

<h3><strong>Example 1:</strong><h3><br>
<img src = "https://assets.leetcode.com/uploads/2023/05/28/example.png">
<h3><strong>Input:</strong></h3> <span><p>head = [1,8,9]</p></span>
<h3><strong>Output:</strong></h3> <span><p>[3,7,8]</p></span>
<h3><strong>Explanation:</strong></h3> <span><p>The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.</p></span>

<h3><strong>Example 2:</strong><h3><br>
<img src = "https://assets.leetcode.com/uploads/2023/05/28/example2.png">
<h3><strong>Input:</strong><h3> <span><p>head = [9,9,9]</p></span>
<h3><strong>Output:</strong></h3> <span><p>[1,9,9,8]</p></span>
<h3><strong>Explanation:</strong></h3> <span><p>The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.</p></span>

<h3>Constraints:</h3>

- The number of nodes in the list is in the range <code>[1, 104]</code>
- <code>0 <= Node.val <= 9</code>
- The input is generated such that the list represents a number that does not have leading zeros, except the number <code>0</code> itself.

