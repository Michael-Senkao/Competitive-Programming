[1074. Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target)

Given a <code>matrix</code> and a <code>target</code>, return the number of non-empty submatrices that sum to target.

A submatrix <code>x1, y1, x2, y2</code> is the set of all cells <code>matrix[x][y]</code> with <code>x1 <= x <= x2</code> and <code>y1 <= y <= y2</code>.
Two submatrices <code>(x1, y1, x2, y2)</code> and <code>(x1', y1', x2', y2')</code> are different if they have some coordinate that is different: for example, if <code>x1 != x1'</code>.

### **Example 1:**
<img src = "https://assets.leetcode.com/uploads/2020/09/02/mate1.jpg" />
<pre>
<strong>Input:</strong> matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0<br>
<strong>Output:</strong> 4<br>
<strong>Explanation:</strong> The four 1x1 submatrices that only contain 0.
  </pre>

### **Example 2:**
<pre>
<strong>Input:</strong> matrix = [[1,-1],[-1,1]], target = 0
<strong>Output:</strong> 5
<strong>Explanation:</strong> The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
  </pre>

### **Example 3:**

<strong>Input:</strong> matrix = [[904]], target = 0
<strong>Output:</strong> 0
 

### **Constraints:**

- <code>1 <= matrix.length <= 100</code>
- <code>1 <= matrix[0].length <= 100</code>
- <code>-1000 <= matrix[i][j] <= 1000</code>
- <code>-10^8 <= target <= 10^8</code>
