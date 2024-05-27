# [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number)

The <strong>Fibonacci numbers</strong>, commonly denoted <code>F(n)</code> form a sequence, called the <strong>Fibonacci sequence</strong,
such that each number is the sum of the two preceding ones, starting from <code>0</code> and <code>1</code>. That is,
<pre>
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
  </pre>
  
Given <code>n</code>, calculate <code>F(n)</code>.

### **Example 1:**
<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>
### **Example 2:**
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>
### **Example 3:**
<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
 </pre>

### **Constraints:**

- <code>0 <= n <= 30</code>
