# [Operations on graph](https://basecamp.eolymp.com/en/problems/2472)

Create an undirected graph that supports the next operations:

1. <code>AddEdge(u, v)</code< - add to the graph an edge between the vertices <code>(u, v)</code>;

2. <code>Vertex(u)</code> - print the list of vertices, adjacent with the vertex <code>u</code>.

There is <strong>no loops<strong> and multiple edges in the graph.

### **Input:**

The first line contains the number of vertices in a graph <code>n</code> <code>(1 ≤ n ≤ 10<sup>5</sup>)</code>. 
The next line contains the number of operations <code>k</code> <code>(0 ≤ k ≤ 10<sup>6</sup>)</code>. 
Each next line describes the operation in format: <code>"1 <number> <number>"</code> or <code>"2 <number>"</code>, representing 
respectively the operation <code>AddEdge(u, v)</code> and <code>Vertex(u)</code>.

It is guaranteed that the total amount of numbers to be printed during all operations Vertex, does not exceed <code>2 * 10<sup>5</sup>.

### **Output:**

For each operation Vertex print in a separate line the list of adjacent vertices for a given vertex. 
The vertices in a list can be printed in any order. If some vertex hasn't adjacent vertices, print the empty line.

<img src="https://static.e-olymp.com/content/68/68f5a83aaf9717053999fd0f88c9a1c40c49e797.gif" />

### **Examples:**

<strong>Input #1</strong>
<pre>
4
4
1 1 2
1 2 3
2 4
2 2
</pre>

<strong>Answer #1</strong>
<pre>
  1 3
</pre>

