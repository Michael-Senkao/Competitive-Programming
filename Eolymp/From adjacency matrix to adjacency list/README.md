# [From adjacency matrix to adjacency list](https://basecamp.eolymp.com/en/problems/3981)

A simple directed graph is given with an adjacency matrix. Print its representation in the form of adjacency list.

### **Input:**

First line contains the number of vertices in a graph <code>n</code> <code>(1≤n≤100)</code>. 
Then the adjacency matrix is given. It is guaranteed that graph does not contain loops.

### **Output:**
Print <code>n</code> lines — the adjacency list of the graph. Print in the <code>i<sup>th</sup></code> line the number of edges adjacent to the <code>i<sup>th</sup></code> vertex, 
and then the vertex numbers where these edges go in <strong>increasing</strong> order.

<img src="https://static.e-olymp.com/content/4d/4df7609ab53a66562ff79b1398cba1d0974c5685.gif" />

### **Examples:**

<strong>Input #1</strong>
<pre>
5
0 0 1 0 0
1 0 1 0 0
0 0 0 0 1
1 1 0 0 0
1 1 0 0 0
</pre>

<strong>Answer #1</strong>
<pre>
1 3
2 1 3
1 5
2 1 2
2 1 2
</pre>
