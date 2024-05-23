# [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures)

Given an array of integers <code>temperatures</code> represents the daily temperatures, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code>
<em>is the number of days you have to wait after the</em> <code>i<sup>th</sup><code> <em>day to get a warmer temperature</em>. If there is no future day for which this is possible, keep <code>answer[i] == 0</code> instead.

### **Example 1:**
<pre>
<strong>Input:</strong> temperatures = [73,74,75,71,69,72,76,73]
<strong>Output:</strong> [1,1,4,2,1,1,0,0]
</pre>

### **Example 2:**
<pre>
<strong>Input:</strong> temperatures = [30,40,50,60]
<strong>Output:</strong> [1,1,1,0]
  </pre>
  
### **Example 3:**
<pre>
<strong>Input:</strong> temperatures = [30,60,90]
<strong>Output:</strong> [1,1,0]
 </pre>

### **Constraints:**

- <code>1 <= temperatures.length <= 105</code>
- <code>30 <= temperatures[i] <= 100</code>
