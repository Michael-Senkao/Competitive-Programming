# [Equilibrium Point](https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1)

Given an array <code>A</code> of <code>n</code> <strong>non negative numbers</strong>. The task is to find the first <strong>equilibrium point</strong> in an array. 
Equilibrium point in an array is an index (or position) such that the <strong>sum</strong> of all elements <strong>before</strong> that index is <strong>same</strong> 
as <strong>sum</strong> of elements <strong>after</strong> it.

Note: Return equilibrium point in <strong>1-based</strong> indexing. Return <code>-1</code> if no such point exists. 

### **Example 1:**
<pre>
<strong>Input:</strong> 
n = 5 
A[] = {1,3,5,2,2} 
<strong>Output:</strong> 
3 
<strong>Explanation:</strong>  
equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2). 
</pre>
### **Example 2:**
<pre>
<strong>Input:</strong>
n = 1
A[] = {1}
<strong>Output:</strong> 
1
<strong>Explanation:</strong>
Since there's only element hence its only the equilibrium point.
</pre>
<strong>Your Task:</strong>
The task is to complete the function <code>equilibriumPoint()</code> which takes the array and <code>n</code> as input parameters and returns the point of equilibrium. 

<strong>Expected Time Complexity:</strong> O(n) <br />
<strong>Expected Auxiliary Space:</strong> O(1)

### **Constraints:**
- <code>1 <= n <= 10<sup>5</sup></code>
- <code>0 <= A[i] <= 10<sup>9</sup></code>
