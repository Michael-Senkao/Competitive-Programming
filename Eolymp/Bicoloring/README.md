# [Bicoloring](https://basecamp.eolymp.com/en/problems/3165)

In 1976 the "Four Color Map Theorem" was proven with the assistance of a computer. This theorem states that every map can be 
colored using only four colors, in such a way that no region is colored using the same color as a neighbor region.

Here you are asked to solve a simpler similar problem. You have to decide whether a given arbitrary connected graph can be 
bicolored. That is, if one can assign colors (from a palette of two) to the nodes in such a way that no two adjacent nodes 
have the same color. To simplify the problem you can assume:
- no node will have an edge to itself.
- the graph is <strong>nondirected</strong>. That is, if a node <code>a</code> is said to be connected to a node <code>b</code>, then you must assume that <code>b</code> is connected to <code>a</code>.
- the graph will be <strong>connected</strong>. That is, there will be at least one path from any node to any other node.
