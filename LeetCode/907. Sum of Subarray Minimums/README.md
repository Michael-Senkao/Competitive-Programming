# [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums)

Given an array of integers <code>arr</code>, find the sum of <code>min(b)</code>, where <code>b</code> ranges over every (contiguous) subarray of <code>arr</code>. Since the answer may be large, return the answer <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.

Example 1:
<pre>
<strong>Input:</strong> arr = [3,1,2,4]
<strong>Output:</strong> 17
<strong>Explanation:</strong> 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
</pre>

### **Example 2:**
<pre>
<strong>Input:</strong> arr = [11,81,94,43,3]
<strong>Output:</strong> 444
 </pre>

### **Constraints:**

- <code>1 <= arr.length <= 3 * 104</code>
- <code>1 <= arr[i] <= 3 * 104</code>
