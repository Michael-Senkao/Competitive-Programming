## [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

Given a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

 
## **Example 1:**
<pre>
<strong>Input:</strong> s = "()"
<strong>Output:</strong> true
 </pre>
## **Example 2:**
<pre>
<strong>Input:</strong> s = "()[]{}"
<strong>Output:</strong> true
 </pre>
## **Example 3:**
<pre>
<strong>Input:</strong> s = "(]"
<strong>Output:</strong> false
 </pre>

## **Constraints:**

- <code>1 <= s.length <= 104</code>
- <code>s</code> consists of parentheses only <code>'()[]{}'</code>.
