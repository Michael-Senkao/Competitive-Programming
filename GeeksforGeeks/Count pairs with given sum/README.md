# [Count pairs with given sum](https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1)

Given an array of <code>N</code> integers, and an integer <code>K</code>, find the number of <strong>pairs</strong> of elements
in the array whose <strong>sum</strong> is equal to <code>K</code>.


### **Example 1:**
<pre>
<strong>Input:</strong>
N = 4, K = 6
arr[] = {1, 5, 7, 1}
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.
</pre>
### **Example 2:**
<pre>
<strong>Input:</strong>
N = 4, K = 2
arr[] = {1, 1, 1, 1}
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
Each 1 will produce sum 2 with any 1.
</pre>
</strong>Your Task:</strong><br />
You don't need to read input or print anything. Your task is to complete the function <code>getPairsCount()</code>which takes
<code>arr[]</code>, <code>n</code> and <code>k</code> as input parameters and returns the <strong>number of pairs</strong> 
that have sum <code>K</code>.


<strong>Expected Time Complexity:</strong> O(N) <br />
<strong>Expected Auxiliary Space:</strong> O(N)

### **Constraints:**
- <code>1 <= N <= 10<sup>5</sup></code>
- <code>1 <= K <= 10<sup>8</sup></code>
- <code>1 <= Arr[i] <= 10<sup>6</sup></code>
