# [2331. Evaluate Boolean Binary Tree](https://leetcode.com/problems/evaluate-boolean-binary-tree)

You are given the <code>root</code> of a <strong>full binary tree</strong> with the following properties:

- <strong>Leaf nodes</strong> have either the value <code>0</code> or <code>1</code>, where <code>0</code> represents <code>False</code> and <code>1</code> represents <code>True</code>.
- <strong>Non-leaf nodes</strong> have either the value <code>2</code> or <code>3</code>, where <code>2</code> represents the boolean <code>OR</code> and <code>3</code> represents the boolean <code>AND</code>.<br>

The <strong>evaluation</strong> of a node is as follows:

- If the node is a leaf node, the evaluation is the <strong>value</strong> of the node, i.e. <code>True</code> or <code>False</code>.
- Otherwise, <strong>evaluate</strong> the node's two children and <strong>apply</strong> the boolean operation of its value with the children's evaluations.
  
Return <em>the boolean result of evaluating the</em> <code>root</code> <em>node</em>.

A <strong>full binary tree</strong> is a binary tree where each node has either <code>0</code> or <code>2</code> children.

A <strong>leaf node</strong> is a node that has zero children.
