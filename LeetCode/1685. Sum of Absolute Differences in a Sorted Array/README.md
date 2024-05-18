# [1685. Sum of Absolute Differences in a Sorted Array]()https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array

You are given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order.

Build and return <en>an integer array</em> <code>result</code> <em>with the same length as</em> <code>nums</code> <em>such that</em> <code>result[i]</code> <em>is equal to the <strong>summation of absolute differences</strong> between</em> <code>nums[i]</code> <em>and all the other elements in the array</em>.

In other words, <code>result[i]</code> is equal to <code>sum(|nums[i]-nums[j]|)</code> where <code>0 <= j < nums.length</code> and <code>j != i</code> (<strong>0-indexed</strong>).

### **Example 1:**
<pre>
<strong>Input:</strong> nums = [2,3,5]
<strong>Output:</strong> [4,3,5]
<strong>Explanation:</strong> Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
  </pre>
  
### **Example 2:**
<pre>
<strong>Input:</strong>strong> nums = [1,4,6,8,10]
<strong>Output:</strong>strong> [24,15,13,15,21]
 </pre>

### **Constraints:**

- <code>2 <= nums.length <= 105</code>
- <code>1 <= nums[i] <= nums[i + 1] <= 104</code>
