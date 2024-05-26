# [649. Dota2 Senate](https://leetcode.com/problems/dota2-senate)

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. 
The voting for this change is a round-based procedure. In each round, each senator can exercise <strong>one</strong> of the two rights:

- <strong>Ban one senator's right:</strong> A senator can make another senator lose all his rights in this and all the following rounds.
- <strong>Announce the victory:</strong> If this senator found the senators who still have rights to vote are all from the same party, he can announce 
the victory and decide on the change in the game.

Given a string <code>senate</code> representing each senator's party belonging. The character <code>'R'</code> and <code>'D'</code> represent the Radiant party and the Dire party. 
Then if there are <code>n</code> senators, the size of the given string will be <code>n</code>.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. 
All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the 
victory and change the Dota2 game. The output should be <code>"Radiant"</code> or <code>"Dire"</code>.

### **Example 1:**
<pre>
<strong>Input:</strong> senate = "RD"
<strong>Output:</strong> "Radiant"
<strong>Explanation:</strong> 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can 
 vote.
</pre>

### **Example 2:**
<pre>
<strong>Input:</strong> senate = "RDD"
<strong>Output:</strong> "Dire"
<strong>Explanation:</strong> 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can 
 vote.
 </pre>

### **Constraints:**

- <code>n == senate.length</code>
- <code>1 <= n <= 104</code>
- <code>senate[i]</code> is either <code>'R'</code> or <code>'D'</code>.
