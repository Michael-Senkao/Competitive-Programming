# [Masha and a Beautiful Tree](https://codeforces.com/problemset/problem/1741/D)

The girl named Masha was walking in the forest and found a complete binary tree of height <code><em>n</em></code> and a permutation <code><em>p</em></code> of length 
<code><em>m=2<sup>n</sup></em></code>.

A complete binary tree of height <code><em>n</em></code> is a rooted tree such that every vertex except the leaves has exactly 
two sons, and the length of the path from the root to any of the leaves is <code><em>n</em></code>. 
The picture below shows the complete binary tree for <code><em>n = 2</em></code>.

A permutation is an array consisting of <code><em>n</em></code> different integers from <code><em>1</em></code> to <code><em>n</em></code>. 
For example, <code><em>[2,3,1,5,4]</em></code> is a permutation, but <code><em>[1,2,2]</em></code> is not (<code><em>2</em></code> occurs twice), 
and <code><em>[1,3,4]</em></code> is also not a permutation (<code><em>n = 3</em></code>, but there is <code><em>4</em></code> in the array).

Let's enumerate <code><em>m</em></code> leaves of this tree from left to right. The leaf with the number <code><em>i</em></code> contains the value <code><em>p<sub>i</sub> (1 ≤ i ≤ m)</em></code>.

For example, if <code><em>n = 2</em></code>, <code><em>p = [3,1,4,2]</em></code>, the tree will look like this:

<img src="https://espresso.codeforces.com/7659f6baa10b482f16f752446d8296b98fd6ae64.png" />

