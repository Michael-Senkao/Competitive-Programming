# [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i)

The <strong>next greater element</strong> of some element <code>x</code> in an array is the <strong>first greater</strong> element that is <strong>to the right</strong> of <code>x<code> in the same array.

You are given two <strong>distinct 0-indexed</strong> integer arrays <code>nums1</code> and <code>nums2</code>, where <code>nums1</code> is a subset of <code>nums2</code>.

For each <code>0 <= i < nums1.length</code>, find the index <code>j</code> such that <code>nums1[i] == nums2[j]</code> and determine the <strong>next greater element</strong> of <code>nums2[j]</code> in <code>nums2</code>. If there is no next greater element, then the answer for this query is <code>-1</code>.

Return <em>an array <code>ans</code> of length <code>nums1.length</code> such that <code>ans[i]</code> is the <strong>next greater element</strong> as described above</em>.

### **Example 1:**
<pre>
<strong>Input:</strong> nums1 = [4,1,2], nums2 = [1,3,4,2]
<strong>Output:</strong> [-1,3,-1]
<strong>Explanation:</strong> The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
</pre>

### **Example 2:**
<pre>
<strong>Input:</strong> nums1 = [2,4], nums2 = [1,2,3,4]
<strong>Output:</strong> [3,-1]
<strong>Explanation:</strong> The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
</pre>

### **Constraints:**

- <code>1 <= nums1.length <= nums2.length <= 1000</code>
- <code>0 <= nums1[i], nums2[i] <= 104</code>
- All integers in <code>nums1</code> and <code>nums2</code> are <strong>unique</strong>.
- All the integers of <code>nums1</code> also appear in <code>nums2</code>.
