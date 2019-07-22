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

