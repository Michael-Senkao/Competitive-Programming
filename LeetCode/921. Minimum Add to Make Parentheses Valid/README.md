# [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid)

A parentheses string is valid if and only if:

- It is the empty string,
- It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or
- It can be written as <code>(A)</code>, where <code>A</code> is a valid string.
  
You are given a parentheses string <code>s</code>. In one move, you can insert a parenthesis at any position of the string.

- For example, if <code>s = "()))"</code>, you can insert an opening parenthesis to be "(()))" or a closing parenthesis to
  be <code>"())))"</code>.
  
Return <em>the minimum number of moves required to make <code>s</code> valid</em>.

### **Example 1:**
<pre>
<strong>Input:</strong> s = "())"
<strong>Output:</strong> 1
  </pre>
### **Example 2:**
<pre>
<strong>Input:</strong> s = "((("
<strong>Output:</strong> 3
 </pre>

### **Constraints:**

- <code>1 <= s.length <= 1000</code>
- <code>s[i]</code> is either <code>'('</code> or <code>')'</code>.
