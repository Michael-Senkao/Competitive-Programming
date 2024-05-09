<h1><a href = "https://leetcode.com/problems/maximize-happiness-of-selected-children">3075. Maximize Happiness of Selected Children</a></h1>

You are given an array <code>happiness</code> of length <code>n</code>, and a <strong>positive</strong> integer <code>k</code>.

There are <code>n</code> children standing in a queue, where the i<code>i<sup>th</sup></code> child has <strong>happiness value</strong> <code>happiness[i]</code>. You want to select <code>k</code> children from these <code>n</code> children in <code>k</code> turns.

In each turn, when you select a child, the <strong>happiness value</strong> of all the children that have <strong>not</strong> been selected till now decreases by <code>1</code>. Note that the happiness value <strong>cannot</strong> become negative and gets decremented <strong>only</strong> if it is positive.

<em>Return the</em> <strong>maximum</code> <em>sum of the happiness values of the selected children you can achieve by selecting</em> <code>k</code> <em>children.</em>

 

## Example 1:

<strong>Input:</strong> happiness = [1,2,3], k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> We can pick 2 children in the following way:
- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
The sum of the happiness values of the selected children is 3 + 1 = 4.
## Example 2:

<strong>Input:</strong> happiness = [1,1,1,1], k = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can pick 2 children in the following way:
- Pick any child with the happiness value == 1. The happiness value of the remaining children becomes [0,0,0].
- Pick the child with the happiness value == 0. The happiness value of the remaining child becomes [0,0].
The sum of the happiness values of the selected children is 1 + 0 = 1.
## Example 3:

<strong>Input:</strong> happiness = [2,3,4,5], k = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> We can pick 1 child in the following way:
- Pick the child with the happiness value == 5. The happiness value of the remaining children becomes [1,2,3].
The sum of the happiness values of the selected children is 5.
 

## Constraints:

- <code>1 <= n == happiness.length <= 2 * 105</code>
- <code>1 <= happiness[i] <= 108</code>
= <code>1 <= k <= n</code>
