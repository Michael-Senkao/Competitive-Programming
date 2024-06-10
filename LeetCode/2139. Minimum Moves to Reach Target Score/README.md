# [2139. Minimum Moves to Reach Target Score](https://leetcode.com/problems/minimum-moves-to-reach-target-score)

You are playing a game with integers. You start with the integer <code>1</code> and you want to reach the integer <code>target</code>.

In one move, you can either:

- <strong>Increment</strong> the current integer by one (i.e., <code>x = x + 1</code>).
- <strong>Double</strong> the current integer (i.e., <code>x = 2 * x</code>).
  
You can use the <strong>increment</strong> operation <strong>any</strong> number of times, however, you can only use the double operation 
at most <code>maxDoubles</code> times.

Given the two integers <code>target</code> and <code>maxDoubles</code>, return <em>the minimum number of moves needed to reach</em> <code>target</code> 
<em>starting</em> with <code>1</code>.

### **Example 1:**
<pre>
<strong>Input:</strong> target = 5, maxDoubles = 0
<strong>Output:</strong> 4
<strong>Explanation:</strong> Keep incrementing by 1 until you reach target.
</pre>
### **Example 2:**
<pre>
<strong>Input:</strong> target = 19, maxDoubles = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> Initially, x = 1
Increment 3 times so x = 4
Double once so x = 8
Increment once so x = 9
Double again so x = 18
Increment once so x = 19
</pre>
### **Example 3:**
<pre>
<strong>Input:</strong> target = 10, maxDoubles = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong> Initially, x = 1
Increment once so x = 2
Double once so x = 4
Increment once so x = 5
Double again so x = 10
 </pre>

### **Constraints:**

- <code>1 <= target <= 10<sup>9</sup></code>
- <code>0 <= maxDoubles <= 100</code>
