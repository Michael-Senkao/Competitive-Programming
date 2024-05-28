# [486. Predict the Winner](https://leetcode.com/problems/predict-the-winner)

You are given an integer array <code>nums</code>. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of <code>0</code>. 
At each turn, the player takes one of the numbers from either end of the array (i.e., <code>nums[0]</code> or <code>nums[nums.length - 1]</code>) 
which reduces the size of the array by <code>1</code>. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return <code>true</code> if Player 1 can win the game. If the scores of both players are equal, then player 1 
is still the winner, and you should also return <code>true</code>. 
You may assume that both players are playing optimally.

### **Example 1:**
<pre>
<strong>Input:</strong> nums = [1,5,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 
 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.
</pre>
### **Example 2:**
<pre>
<strong>Input:</strong> nums = [1,5,233,7]
<strong>Output:</strong> true
<strong>Explanation:</strong> Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter 
 which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 
 can win.
 </pre>

### **Constraints:**

- <code>1 <= nums.length <= 20</code>
- <code>0 <= nums[i] <= 107</code>
