# [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue)

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on 
FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, 
we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the <code>MyCircularQueue</code> class:

- <code>MyCircularQueue(k)</code> Initializes the object with the size of the queue to be <code>k</code>.
- <code>int Front()</code> Gets the front item from the queue. If the queue is empty, return <code>-1</code>.
- <code>int Rear()</code> Gets the last item from the queue. If the queue is empty, return <code>-1</code>.
- <code>boolean enQueue(int value)</code> Inserts an element into the circular queue. Return <code>true</code> if the operation is successful.
- <code>boolean deQueue()</code> Deletes an element from the circular queue. Return <code>true</code> if the operation is successful.
- <code>boolean isEmpty()</code> Checks whether the circular queue is empty or not.
- <code>boolean isFull()</code> Checks whether the circular queue is full or not.
  
You must solve the problem without using the built-in queue data structure in your programming language. 

### **Example 1:**
<pre>
<strong>Input</strong>
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
<strong>Output</strong>
[null, true, true, true, false, 3, true, true, true, 4]

<strong>Explanation</strong>
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 </pre>

### **Constraints:**

- <code>1 <= k <= 1000</code>
- <code>0 <= value <= 1000</code>
- At most <code>3000</code> calls will be made to <code>enQueue</code>, <code>deQueue</code>, <code>Front</code>, <code>Rear</code>,
- <code>isEmpty</code>, and <code>isFull</code>.
