from collections import deque


# maxlen: represents the number of elements that this queue can hold,
# Once determined, it cannot be modified.
dq = deque(range(10), maxlen=10)
print(dq)

# the rotation of the queue accept a parameter n, when n > 0, the rightmost n elements of
# the queue are moved to the left of the queue; when n < 0, the leftmost n elements are
# moved to the right
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)

# when trying to do a tail(header) add operation on a queue that is full, at the time, the elements
# in its header(tail) will be deleted.
dq.appendleft(-1)
print(dq)
dq.append(10)
print(dq)
dq.extend([11,12,13])
print(dq)

# the extendleft(iter) method adds the elements of the iterator to the two-way queue one by one.
# on the left side, the elements in the iterator will appear in the queue in reverse order.
dq.extendleft([-1,-2,-3])
print(dq)
