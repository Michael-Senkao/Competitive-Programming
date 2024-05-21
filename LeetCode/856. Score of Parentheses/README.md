# [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses)

Given a balanced parentheses string <code>s</code>, return <em>the <strong>score</strong> of the string</em>.

The <strong>score</strong> of a balanced parentheses string is based on the following rule:

- <code>"()"</code> has score <code>1</code>.
- <code>AB</code> has score <code>A + B</code>, where <code>A</code> and <code>B</code> are balanced parentheses strings.
- <code>(A)</code> has score <code>2 * A</code>, where <code>A</code> is a balanced parentheses string.

### **Example 1:**
<pre>
<strong>Input:</strong> s = "()"
<strong>Output:</strong> 1
</pre>

### **Example 2:**
<pre>
<strong>Input:</strong> s = "(())"
<strong>Output:</strong> 2
</pre>

### **Example 3:**
<pre>
<strong>Input:</strong> s = "()()"
<strong>Output:</strong> 2
 </pre>

### **Constraints:**

- <code>2 <= s.length <= 50</code>
- <code>s</code> consists of only <code>'('</code> and <code>')'</code>.
- <code>s</code> is a balanced parentheses string.
