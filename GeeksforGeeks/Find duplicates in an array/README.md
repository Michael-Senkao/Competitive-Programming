# [Find duplicates in an array](https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1)

Given an array <code>a</code> of size <code>N</code> which contains elements from <code>0</code> to <code>N-1</code>, you need to find <strong>all</strong> the elements occurring 
<strong>more than once</strong> in the given array. 
Return the answer in <strong>ascending order</strong>. If no such element is found, return list containing <code>[-1]</code>. 

<strong>Note:</strong> The extra space is only for the array to be returned. Try and perform all operations within the provided array. 

### **Example 1:**
<pre>
<strong>Input:</strong>
N = 4
a[] = {0,3,1,2}
<strong>Output:</strong> 
-1
<strong>Explanation:</strong> 
There is no repeating element in the array. Therefore output is -1.
  </pre>
### **Example 2:**
<pre>
</trong>Input:</strong>
N = 5
a[] = {2,3,1,2,3}
<strong>Output:</strong> 
2 3 
<strong>Explanation:</strong> 
2 and 3 occur more than once in the given array.
</pre>
Your Task:
Complete the function duplicates() which takes array a[] and n as input as parameters and returns a list of elements that occur more than once in the given array in a sorted manner. 

<strong>Expected Time Complexity:</strong> O(n). <br />
<strong>Expected Auxiliary Space:</strong> O(n).

### **Constraints:**
- <code>1 <= N <= 105</code>
- <code>0 <= A[i] <= N-1</code>, for each valid <code>i</code>
