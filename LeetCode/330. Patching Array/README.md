# [330. Patching Array](https://leetcode.com/problems/patching-array)

Given a sorted integer array <code>nums</code> and an integer <code>n</code>, add/patch elements to the array such that any number in the range <code>[1, n]</code> 
inclusive can be formed by the sum of some elements in the array.

Return <em>the minimum number of patches required</em>.

### **Example 1:**
<pre>
<strong>Input:</strong> nums = [1,3], n = 6
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
</pre>pre>
### **Example 2:**
<pre>
<strong>Input:</strong> nums = [1,5,10], n = 20
<strong>Output:</strong> 2
<strong>Explanation:</strong> The two patches can be [2, 4].
</pre>pre>
### **Example 3:**
<pre>
<strong>Input:</strong> nums = [1,2,2], n = 5
<strong>Output:</strong> 0
 </pre>

### **Constraints:**

- <code>1 <= nums.length <= 1000</code>
- <code>1 <= nums[i] <= 10<sup>4</sup></code>
- <code>nums</code> is sorted in <strong>ascending order</strong>.
- <code>1 <= n <= 2<sup>31</sup> - 1</code>
