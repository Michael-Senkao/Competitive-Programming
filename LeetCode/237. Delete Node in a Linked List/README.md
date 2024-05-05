<h2> <a href="https://leetcode.com/problems/delete-node-in-a-linked-list/">237. Delete Node in a Linked List</a> </h2>

<p>There is a singly-linked list <code>head</code> and we want to delete a node <code>node</code> in it.</p>
<p>You are given the node to be deleted <code>node</code>. You will <strong>not be given access</strong> to the first node of <code>head</code>.</p>
<p>All the values of the linked list are <strong>unique</strong>, and it is guaranteed that the given node <code>node</code> is not the last node in the linked list.</p>
<p>Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:</p>
<ul>
  <li>The value of the given node should not exist in the linked list.</li>
  <li>The number of nodes in the linked list should decrease by one.</li>
  <li>All the values before node should be in the same order.</li>
  <li>All the values after node should be in the same order.</li>
</ul>
<p><strong>Custom testing:</strong></p>
<ul>
  <li>For the input, you should provide the entire linked list <code>head</code> and the node to be given <code>node</code>. <code>node</code> should not be the last node of the list and should be an actual node in the list.</li>
  <li>We will build the linked list and pass the node to your function.</li>
  <li>The output will be the entire list after calling your function.</li>
</ul>
