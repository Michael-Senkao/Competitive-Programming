There are <code>n</code> people in a line queuing to buy tickets, where the <code>0th</code> person is 
at the <strong>front</strong> of the line and the <code>(n - 1)th</code> person is at the <strong>back</strong> of the line.

You are given a <strong>0-indexed</strong> integer array <code>tickets</code> of length <code>n</code> where the number of tickets that the <code>ith</code> person would like to buy is 
<code>tickets[i]</code>.

Each person takes <strong>exactly 1 second</strong> to buy a ticket. A person can only buy <strong>1 ticket at a time</strong> and has to go back to <strong>the end</strong> of the
line (which happens <strong>instantaneously</strong>) in order to buy more tickets. If a person does not have any tickets left to buy, the person will <strong>leave</strong> the line.

Return <em>the <strong>time taken</strong> for the person at position <code>k</code> <strong>(0-indexed)</strong> to finish buying tickets</em>.

### **Example 1:**
<pre>
<strong>Input:</strong> tickets = [2,3,2], k = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
</pre>
### **Example 2:**
<pre>
<strong>Input:</strong> tickets = [5,1,1,1], k = 0
<strong>Output:</strong> 8
<strong>Explanation:</strong>
- In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
- In the next 4 passes, only the person in position 0 is buying tickets.
The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.
 </pre>

### **Constraints:**

- <code>n == tickets.length</code>
- <code>1 <= n <= 100</code>
- <code>1 <= tickets[i] <= 100</code>
- <code>0 <= k < n</code>
