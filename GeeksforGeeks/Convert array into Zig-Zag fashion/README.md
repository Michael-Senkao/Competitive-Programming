# [Convert array into Zig-Zag fashion](https://www.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion1638/1)

Given an array <code>arr</code> of <strong>distinct</strong> elements of size <code>n</code>, the task is to rearrange the 
elements of the array in a <strong>zig-zag</strong> fashion so that the converted array should be in the below form: 

<code>arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]</code>. 

<strong>Note:</strong> Modify the given <code>arr[]</code> only, If your transformation is correct, 
the output will be <code>1</code> else the output will be <code>0</code>. 

### **Examples:**
<pre>
  <strong>Input:</strong> n = 7, arr[] = {4, 3, 7, 8, 6, 2, 1}
  <strong>Output:</strong> 1
  <strong>Explanation:</strong>  After modification the array will look like 3 < 7 > 4 < 8 > 2 < 6 > 1, the checker in the driver code will produce 1.
</pre>
<pre>
  <strong>Input:</strong> n = 5, arr[] = {4, 7, 3, 8, 2}
  <strong>Output:/strong> 1
<strong>Explanation:</strong> After modification the array will look like 4 < 7 > 3 < 8 > 2 hence output will be 1.
</pre>

<strong>Expected Time Complexity:</strong> O(n)<br />
<strong>Expected Auxiliary Space:</strong> O(1)

### **Constraints:**
- <code>1 <= n <= 10<sup>6</sup></code>
- <code>0 <= arr<sub>i</sub> <= 10<sup>9</sup></code>
