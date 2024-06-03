# [Second Largest](https://www.geeksforgeeks.org/problems/second-largest3735/1)

Given an array <code>Arr</code> of size <code>N</code>, print the <strong>second largest distinct element</strong> from an array. 
If the second largest element <strong>doesn't</strong> exist then return <code>-1</code>.

### **Example 1:**
<pre>
<strong>Input:</strong> 
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}
<strong>Output:</strong> 34
<strong>Explanation:</strong> The largest element of the array is 35 and the second largest elementis 34.
</pre>
### **Example 2:**
<pre>
<strong>Input:</strong> 
N = 3
Arr[] = {10, 5, 10}
<strong>Output:</strong> 5
</strong>Explanation:</strong> The largest element of the array is 10 and the second largest element is 5.
</pre>
<strong>Your Task:</strong>
You don't need to read input or print anything. Your task is to complete the function <code>print2largest()</code> which takes 
the array of integers <code>arr</code> and <code>n</code> as parameters and returns an integer denoting the answer.
If <strong>2nd largest</strong> element <strong>doesn't</strong> exist then return <code>-1</code>.

<strong>Expected Time Complexity:</strong> O(N) <br />
<strong>Expected Auxiliary Space:</strong> O(1)

### **Constraints:**
- <code>2 ≤ N ≤ 10<sup>5</sup></code>
- <code>1 ≤ Arr<sub>i</sub> ≤ 10<sup>5</sup></code>
