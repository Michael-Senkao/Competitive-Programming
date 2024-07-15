# [Bicoloring](https://basecamp.eolymp.com/en/problems/3165)

In 1976 the "Four Color Map Theorem" was proven with the assistance of a computer. This theorem states that every map can be 
colored using only four colors, in such a way that no region is colored using the same color as a neighbor region.

Here you are asked to solve a simpler similar problem. You have to decide whether a given arbitrary connected graph can be 
bicolored. That is, if one can assign colors (from a palette of two) to the nodes in such a way that no two adjacent nodes 
have the same color. To simplify the problem you can assume:
- no node will have an edge to itself.
- the graph is <strong>nondirected</strong>. That is, if a node <code>a</code> is said to be connected to a node <code>b</code>, then you must assume that <code>b</code> is connected to <code>a</code>.
- the graph will be <strong>connected</strong>. That is, there will be at least one path from any node to any other node.

### **Input:**

Consists of several test cases. Each test case starts with a line containing the number <code>n (0≤n≤1000)</code> of different nodes. The second line contains the number of edges <code>l (1≤l≤250000)</code>. After this <code>l</code> lines will follow, each containing two numbers that specify an edge between the two nodes that they represent. A node in the graph will be labeled using a number <code>a (1≤a≤n)</code>. The last test contains <code>n=0</code> and is not to be processed.

### **Output:**
You have to decide whether the input graph can be bicolored or not, and print it as shown below.

<img src="https://static.e-olymp.com/content/24/249b876dd10ab00c90c099f5775f9c2fcc84593b.gif" />

### **Examples:**
<strong>Input #1</strong>
<pre>
3
3
1 2
2 3
3 1
8
12
1 2
2 4
3 4
3 1
3 7
7 6
4 6
1 6
2 5
5 6
4 8
5 8
0
</pre>
<strong>Answer #1</strong>
<pre>
NOT BICOLOURABLE.
BICOLOURABLE.
</pre>
