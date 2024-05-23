# [456. 132 Pattern](https://leetcode.com/problems/132-pattern)

Given an array of <code>n</code> integers <code>nums</code>, a <strong>132 pattern</strong> is a subsequence of three integers <code>nums[i]</code>, <code>nums[j]</code> and <code>nums[k]</code> such that <code>i < j < k</code> and <code>nums[i] < nums[k] < nums[j]</code>.

Return <code>true</code> <em>if there is a <strong>132 pattern</strong> in <code>nums</code>, otherwise, return <code>false</code></em>.

### **Example 1:**
<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no 132 pattern in the sequence.
</pre>
  
### **Example 2:**
<pre>
<strong>Input:</strong> nums = [3,1,4,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a 132 pattern in the sequence: [1, 4, 2].
</pre>
  
### **Example 3:**
<pre>
<strong>Input:</strong> nums = [-1,3,2,0]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 </pre>

### **Constraints:**

- <code>n == nums.length</code>
- <code>1 <= n <= 2 * 105</code>
- <code>-109 <= nums[i] <= 109</code>
