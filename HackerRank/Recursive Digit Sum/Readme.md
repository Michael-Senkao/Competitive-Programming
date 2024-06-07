# [Recursive Digit Sum]()

We define super digit of an integer <code>x</code> using the following rules:

Given an integer, we need to find the super digit of the integer.

- If <code>x</code> has only <code>1</code> digit, then its super digit is <code>x</code>.
- Otherwise, the super digit of <code>x</code> is equal to the super digit of the sum of the digits of <code>x</code>.

For example, the super digit of <code>9875</code> will be calculated as:
<pre>
  super_digit(9875)   	9+8+7+5 = 29 
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2  
</pre>

### **Example:**
n = '9875'
k = 4

The number <code>p</code> is created by concatenating the string <code>n</code> <code>k</code> times so the initial 
<code>p = 9875987598759875</code>.
<pre>
superDigit(p) = superDigit(9875987598759875)
                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    superDigit(p) = superDigit(116)
                  1+1+6 = 8
    superDigit(p) = superDigit(8)
</pre>
All of the digits of p sum to <code>116</code>. The digits of <code>116</code> sum to <code>8</code>. <code>8</code> is only one digit, 
so it is the super digit.

### **Function Description:**

Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):

- string n: a string representation of an integer
- int k: the times to concatenate <code>n</code> to make <code>p</code>

### **Returns:**

- int: the super digit of <code>n</code> repeated <code>k</code> times

### **Input Format:**
The first line contains two space separated integers, <code>n</code>and <code>k</code>.

### **Constraints:**
- <code>1 <= n < 10<sup>100000</sup></code>
- <code>1 <= k <= 10<sup>5</sup></code>
