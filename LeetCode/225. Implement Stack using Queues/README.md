# [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues)

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (<code>push</code>, <code>top</code>, <code>pop</code>, and <code>empty</code>).

Implement the <code>MyStack</code> class:

- <code>void push(int x)</code> Pushes element x to the top of the stack.
- <code>int pop()</code> Removes the element on the top of the stack and returns it.
- <code>int top()</code> Returns the element on the top of the stack.
- <code>boolean empty()</code> Returns <code>true</code> if the stack is empty, <code>false</code> otherwise.
  
#### **Notes:**

- You must use <strong>only</strong> standard operations of a queue, which means that only <code>push to back</code>, <code>peek/pop from front</code>, <code>size</code> and <code>is empty</code> operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

### **Example 1:**
<pre>
**Input**
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

**Output**
[null, null, null, 2, 2, false]

**Explanation**
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
</pre> 

### **Constraints:**

- <code>1 <= x <= 9</code>
- At most <code>100</code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, and <code>empty</code>.
- All the calls to <code>pop</code> and <code>top</code> are valid.
