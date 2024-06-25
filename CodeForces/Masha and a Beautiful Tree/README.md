# [Masha and a Beautiful Tree](https://codeforces.com/problemset/problem/1741/D)

The girl named Masha was walking in the forest and found a complete binary tree of height <code>n</code> and a permutation <code>p</code> of length 
<code>m=2<sup>n</sup></code>.

A complete binary tree of height <code>n</code> is a rooted tree such that every vertex except the leaves has exactly 
two sons, and the length of the path from the root to any of the leaves is <code>n</code>. 
The picture below shows the complete binary tree for <code>n = 2</code>.

A permutation is an array consisting of <code>n</code> different integers from <code>1</code> to <code>n</code>. 
For example, <code>[2,3,1,5,4]</code> is a permutation, but <code>[1,2,2]</code> is not (<code>2</code> occurs twice), 
and <code>[1,3,4]</code> is also not a permutation (<code>n = 3</code>, but there is <code>4</code> in the array).

Let's enumerate <code>m</code> leaves of this tree from left to right. The leaf with the number <code>i</code> contains the value <code>p<sub>i</sub> (1 ≤ i ≤ m)</code>.

For example, if <code>n = 2</code>, <code>p = [3,1,4,2]</code>, the tree will look like this:

<img src="https://espresso.codeforces.com/7659f6baa10b482f16f752446d8296b98fd6ae64.png" />

Masha considers a tree beautiful if the values in its leaves are ordered from left to right in increasing order.

In one operation, Masha can choose any non-leaf vertex of the tree and swap its left and right sons (along with their subtrees).

For example, if Masha applies this operation to the root of the tree discussed above, it will take the following form:

<img src="https://espresso.codeforces.com/2806ce5f37676791482074d582abe979125794e9.png" />

Help Masha understand if she can make a tree strong><em>beautiful</em></strong> in a certain number of operations. If she can, then output the minimum number of operations to make the tree <strong><em>beautiful</em></strong>.

### **Input:**
The first line contains single integer <code>t (1 ≤ t ≤ 10<sup>4</sup>)</code> — number of test cases.

In each test case, the first line contains an integer <code>m (1≤m≤262144)</code>, which is a power of two  — the size of the permutation <code>p</code>.

The second line contains m integers: <code>p<sub>1</sub>,p<sub>2</sub>,…,p<sub>m</sub> (1≤p<sub>i</sub>≤m)</code> — the permutation <code>p</code>.

It is guaranteed that the sum of <code>m</code> over all test cases does not exceed <code>3⋅10<sup>5</sup></code>.

### **Output:**
For each test case in a separate line, print the minimum possible number of operations for which Masha will be able to make the tree code>beautiful</code> or <code>-1</code>, if this is not possible.

### **Example:**
<pre>
  <strong>input:</strong>
    4
    8
    6 5 7 8 4 3 1 2
    4
    3 1 4 2
    1
    1
    8
    7 8 4 3 1 2 6 5
  
  <strong>output:</strong>
    4
    -1
    0
    -1
</pre>
