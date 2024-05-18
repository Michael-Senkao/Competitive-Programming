## [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls)

You have a <code>RecentCounter</code> class which counts the number of recent requests within a certain time frame.

Implement the <code>RecentCounter</code> class:

- <code>RecentCounter()</code> Initializes the counter with zero recent requests.
- <code>int ping(int t)</code> Adds a new request at time <code>t</code>, where <code>t</code> represents some time in milliseconds, and returns the number of requests
  that has happened in the past <code>3000</code> milliseconds (including the new request). Specifically, return the number of requests that have
  happened in the inclusive range <code>[t - 3000, t]</code>.
  
It is <strong>guaranteed</strong> that every call to <code>ping</code> uses a strictly larger value of <code>t</code> than the previous call.

### **Example 1:**
<pre>
<strong>Input</strong>strong>
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
  
<strong>Output</strong>strong>
[null, 1, 2, 3, 3]

<strong>Explanation</strong>strong>
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
 </pre>

### **Constraints:**

- <code>1 <= t <= 109</code>
- Each test case will call <code>ping</code> with strictly increasing values of <code>t</code>.
- At most <code>104</code> calls will be made to <code>ping</code>.
