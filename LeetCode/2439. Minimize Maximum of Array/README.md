# [2439. Minimize Maximum of Array](https://leetcode.com/problems/minimize-maximum-of-array)

You are given a <strong>0-indexed</strong> array <code>nums</code> comprising of <code>n</code> non-negative integers.

In one operation, you must:

- Choose an integer <code>i</code> such that <code>1 <= i < n</code> and <code>nums[i] > 0</code>.
- Decrease nums[i] by 1.
- Increase nums[i - 1] by 1.
  
Return <em>the <strong>minimum</strong> possible value of the <strong>maximum</strong> integer of nums after performing <strong>any</strong> number of operations</em>.
