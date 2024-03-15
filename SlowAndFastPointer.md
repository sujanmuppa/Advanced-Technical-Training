# Given a Linked list where there is a loop, find the start of the loop.
## This is a detailed explanation of each and every point in this concept.

Given a linked list, we can find the start of the loop using the Floyd's cycle-finding algorithm. This algorithm is also known as the "tortoise and hare" algorithm. It is used to detect a cycle in a linked list.

The algorithm works by using two pointers, one slow and one fast. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a cycle in the linked list, the two pointers will eventually meet at some point.

To find the start of the loop, we can use the following steps:

1. Initialize two pointers, slow and fast, to the head of the linked list.
2. Move the slow pointer one step at a time and the fast pointer two steps at a time.
3. When the two pointers meet, reset the slow pointer to the head of the linked list.
4. Move the slow and fast pointers one step at a time until they meet again.    
5. The point where the two pointers meet is the start of the loop.

Here is a Python implementation of the algorithm:

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None
```

In this implementation, we use the ListNode class to represent the nodes of the linked list. The detectCycle function takes the head of the linked list as input and returns the start of the loop if it exists, or None if there is no loop.

The algorithm uses two pointers, slow and fast, to traverse the linked list. If there is a loop, the two pointers will eventually meet at some point. We then reset the slow pointer to the head of the linked list and move both pointers one step at a time until they meet again. The point where the two pointers meet is the start of the loop.

The time complexity of this algorithm is O(n), where n is the number of nodes in the linked list. The space complexity is O(1) since we only use a constant amount of extra space.


The reason why this algorithm works is that the distance between the start of the loop and the meeting point of the two pointers is equal to the distance between the head of the linked list and the start of the loop. This is a property of linked lists with loops, and it can be proved using mathematical induction.

The Proof is as follows:

Let's assume that the distance between the head of the linked list and the start of the loop is k, and the distance between the start of the loop and the meeting point of the two pointers is m. Also, let's assume that the length of the loop is l.

When the two pointers meet, the slow pointer has traveled a distance of k + m, and the fast pointer has traveled a distance of k + m + n * l, where n is the number of complete loops the fast pointer has made.

Since the fast pointer moves twice as fast as the slow pointer, we have the following equation:

2 * (k + m) = k + m + n * l

Simplifying the equation, we get:

k + m = n * l

This equation tells us that the distance between the head of the linked list and the start of the loop is equal to the distance between the start of the loop and the meeting point of the two pointers. This is why resetting the slow pointer to the head of the linked list and moving both pointers one step at a time will eventually lead them to the start of the loop.