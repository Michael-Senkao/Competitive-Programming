# [Parenthesis Checker](https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1)

Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".

### **Example 1:**
<pre>
<strong>Input:</strong>
{([])}
<strong>Output:</strong> 
true
<strong>Explanation:</strong> 
{ ( [ ] ) }. Same colored brackets can form 
balanced pairs, with 0 number of 
unbalanced bracket.
</pre>
### **Example 2:**
<pre>
<strong>Input:</strong> 
()
<strong>Output:</strong> 
true
<strong>Explanation:</strong> 
(). Same bracket can form balanced pairs, 
and here only 1 type of bracket is 
present and in balanced way.
</pre>
### **Example 3:**
<pre>
<strong>Input:</strong> 
([]
<strong>Output:</strong> 
false
<strong>Explanation:</strong> 
([]. Here square bracket is balanced but 
the small bracket is not balanced and 
Hence , the output will be unbalanced.
</pre>
<strong>Your Task:</strong>
This is a function problem. You only need to complete the function <code>ispar()</code> that takes a <strong>string</strong> as a parameter and returns a 
<strong>boolean</strong> value <code>true</code> if brackets are balanced else returns <code>false</code>.

<strong>Expected Time Complexity:</strong> O(|x|) <br />
<strong>Expected Auixilliary Space:</strong> O(|x|)

### **Constraints:**
- <code>1 ≤ |x| ≤ 32000</code>
