# [Sources and sinks](https://basecamp.eolymp.com/en/problems/3986)

The vertex of directed graph is called a <code>source</code> if no edge comes into it, and a <code>sink</code> if no edge comes out of it.

The directed graph is given with adjacency matrix. Find all its sources and sinks.

### **Input:**

The first line contains the number of vertices in a graph <code>n</code> <code>(1 ≤ n ≤ 100)</code>, then the adjacent matrix is given - <code>n</code> lines 
with <code>n</code> numbers, each of them equals to <code>0</code> or <code>1</code>.

### **Output:**

Print in the first line the <strong>number</strong> of <code>sources</code> in a graph, and then <code>sources</code> in increasing order. Print in the second line the 
information about <code>sinks</code> in the same format.

<img src="https://static.e-olymp.com/content/ef/ef8a55dafbb041d39eda9274e33b9792167d0d69.gif" />

### **Examples:**

<strong>Input #1</strong>
<pre>
5
0 0 0 0 0
0 0 0 0 1
1 1 0 0 0
0 0 0 0 0
0 0 0 0 0
</pre>

<strong>Answer #1</strong>
<pre>
2 3 4
3 1 4 5
</pre>
