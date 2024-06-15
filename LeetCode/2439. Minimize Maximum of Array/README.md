# [2439. Minimize Maximum of Array](https://leetcode.com/problems/minimize-maximum-of-array)

You are given a <strong>0-indexed</strong> array <code>nums</code> comprising of <code>n</code> non-negative integers.

In one operation, you must:

- Choose an integer <code>i</code> such that <code>1 <= i < n</code> and <code>nums[i] > 0</code>.
- Decrease nums[i] by 1.
- Increase nums[i - 1] by 1.
  
Return <em>the <strong>minimum</strong> possible value of the <strong>maximum</strong> integer of nums after performing <strong>any</strong> number of operations</em>.

### **Example 1:**
<pre>
<strong>Input:</strong> nums = [3,7,1,6]
<strong>Output:</strong> 5
<strong>Explanation:</strong>
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.
</pre>
### **Example 2:**
<pre>
<strong>Input:</strong> nums = [10,1]
<strong>Output:</strong> 10
<strong>Explanation:</strong>
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.
 </pre>

### **Constraints:**

- <code>n == nums.length</code>
- <code>2 <= n <= 10<sup>5</sup></code>
- <code>0 <= nums[i] <= 10<sup>9</sup></code>
