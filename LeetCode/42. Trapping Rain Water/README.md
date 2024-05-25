# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)

Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is <code>1</code>, compute how much water it can trap after raining.

### **Example 1:**
<img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" />
<pre>
  <strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]
  <strong>Output:</strong> 6
  <strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
</pre>

### **Example 2:**
<pre>
<strong>Input:</strong> height = [4,2,0,3,2,5]
<strong>Output:</strong> 9
</pre>

### **Constraints:**

- <code>n == height.length</code>
- <code>1 <= n <= 2 * 104</code>
- <code>0 <= height[i] <= 105</code>
