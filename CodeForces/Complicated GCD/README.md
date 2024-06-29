# [Complicated GCD](https://codeforces.com/contest/664/problem/A)

Greatest common divisor <code>GCD(a, b)</code> of two positive integers <code>a</code> and <code>b</code> is equal to the <strong>biggest integer</strong> <code>d</code> such that both integers 
<code>a</code> and <code>b</code> are divisible by <code>d</code>. There are many efficient algorithms to find greatest common divisor <code>GCD(a, b)</code>, for example, 
Euclid algorithm.

Formally, find the biggest integer d, such that all integers <code>a, a + 1, a + 2, ..., b</code> are divisible by <code>d</code>. To make the problem 
even more complicated we allow <code>a</code> and <code>b</code> to be up to googol, <code>10<sup>100</sup></code> — such number do not fit even in 64-bit integer type!

### **Input:**
The only line of the input contains two integers <code>a</code> and <code>b</code> <code>(1 ≤ a ≤ b ≤ 10100)</code>.

### **Output:**
Output one integer — <strong>greatest common divisor</strong> of all integers from <code>a</code> to <code>b</code> inclusive.

### **Examples:**
<pre>
<strong>input:</strong>
1 2
  
<strong>output:</strong>
1
  
<strong>input:</strong>
61803398874989484820458683436563811772030917980576 61803398874989484820458683436563811772030917980576
  
<strong>output:</strong>
61803398874989484820458683436563811772030917980576
</pre>
