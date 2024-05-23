# [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii)

Given a circular integer array <code>nums</code> (i.e., the next element of <code>nums[nums.length - 1]</code> is <code>nums[0]</code>), return <em>the <strong>next greater number</strong> for every element in</em> <code>nums</code>.

The <strong>next greater number</strong> of a number <code>x</code> is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return <code>-1</code> for this number.

### **Example 1:**
<pre>
<strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> [2,-1,2]
<strong>Explanation:</strong> The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
  </pre>
  
### **Example 2:**
<pre>
<strong>Input:</strong> nums = [1,2,3,4,3]
<strong>Output:/strong> [2,3,4,-1,4]
</pre> 

### **Constraints:**

- <code>1 <= nums.length <= 104</code>
- <code>-109 <= nums[i] <= 109</code>
