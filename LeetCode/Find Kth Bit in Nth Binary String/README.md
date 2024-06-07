# [1545. Find Kth Bit in Nth Binary String](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string)

Given two positive integers <code>n</code> and <code>k</code>, the binary string <code>S<sub>n</sub></code> is formed as follows:

- <code>S1 = "0"</code>
- <code>Si = Si - 1 + "1" + reverse(invert(Si - 1))</code> for <code>i > 1</code>

Where <code>+</code> denotes the concatenation operation, <code>reverse(x)</code> returns the reversed string <code>x</code>, 
and <code>invert(x)</code> inverts all the bits in <code>x</code> (<code>0</code> changes to <code>1</code> and <code>1</code> changes to <code>0</code>).

For example, the first four strings in the above sequence are:

- <code>S1 = "0"</code>
- <code>S2 = "011"</code>
- <code>S3 = "0111001"</code>
- <code>S4 = "011100110110001"</code>
  
Return <em>the</em> <code>k<sup>th</sup></code> <em>bit in</em> <code>S<sub>n</sub></code>. It is guaranteed that <code>k</code> is valid for the given <code>n</code>.

### **Example 1:**
<pre>
<strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> "0"
<strong>Explanation:</strong> S3 is "0111001".
The 1st bit is "0".
  </pre>
### **Example 2:**
<pre>
<strong>Input:</strong> n = 4, k = 11
<strong>Output:</strong> "1"
</strong>Explanation:</strong> S4 is "011100110110001".
The 11th bit is "1".
 </pre>

### **Constraints:**

- <code>1 <= n <= 20</code>
- <code>1 <= k <= 2<sup>n</sup> - 1</code>
