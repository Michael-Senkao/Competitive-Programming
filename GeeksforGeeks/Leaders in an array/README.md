# [Leaders in an array](https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1)

Given an array <code>A</code> of <strong>positive integers</strong>. Your task is to find the <strong>leaders</strong> in the array. 
An element of the array is a leader if it is <strong>greater than all the elements to its right side</strong> or if it is <strong>equal</strong> to the <strong>maximum element</strong> on its right side. 
The rightmost element is always a leader. 

### **Example 1:**
<pre>
<strong>Input:</strong>
n = 6
A[] = {16,17,4,3,5,2}
<strong>Output:</strong> 17 5 2
<strong>Explanation:</strong> The first leader is 17 as it is greater than all the elements to its right.  Similarly, the next leader is 5. 
  The right most element is always a leader so it is also included.
</pre>
### **Example 2:**
<pre>
<strong>Input:</strong>
n = 5
A[] = {10,4,2,4,1}
<strong>Output:</strong> 10 4 4 1
<strong>Explanation:</strong> 1 is the rightmost element and 4 is the element which is greater than all the elements to its right. 
  Similarly another 4 is the element that is equal to the greatest element to its right and 10 is the greatest element in the whole array.

<strong>Your Task:</strong>
You don't need to read input or print anything. The task is to complete the function leader() which takes array A and n as input parameters and 
  returns an array of leaders in order of their appearance.
</pre>
<strong>Expected Time Complexity:</strong> O(n)
<strong>Expected Auxiliary Space:</strong> O(n)

### **Constraints:**
- <code>1 <= n <= 10<sup>7</sup></code>
- <code>0 <= Ai <= 10<sup>7</sup></code>
